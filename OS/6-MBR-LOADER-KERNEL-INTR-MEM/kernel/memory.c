#include "memory.h"
#include "bitmap.h"
#include "stdint.h"
#include "global.h"
#include "print.h"
#include "string.h"
#include "interrupt.h"

#define PG_SIZE 4096
#define MEM_BITMAP_BASE 0xc009a000 // 内存位图的起始地址
#define K_HEAP_START 0xc0100000

#define PDE_IDX(addr) ((addr & 0xffc00000) >> 22) // 虚拟地址高10位, pde
#define PTE_IDX(addr) ((addr & 0x003ff000) >> 12) // 虚拟地址中间10位, pte

struct pool
{
	struct bitmap pool_bitmap;
  	uint32_t phy_addr_start; //本内存池管理的物理内存起始
  	uint32_t pool_size;
};


// 全局变量
struct pool kernel_pool, user_pool;
struct virtual_addr kernel_vaddr;


// 在pf表示的虚拟内存池中申请pg_cnt个虚拟页,成功返回起始地址,失败返回NULL.
static void *vaddr_get(enum pool_flags pf, uint32_t pg_cnt)
{
    int vaddr_start = 0, bit_idx_start = -1;
    uint32_t cnt = 0;
  
    if (pf == PF_KERNEL) // 内核内存池
    {
        bit_idx_start = bitmap_scan(&kernel_vaddr.vaddr_bitmap, pg_cnt);
        if (bit_idx_start == -1)
        {
            return NULL;
        }
        while (cnt < pg_cnt)
        {
            bitmap_set(&kernel_vaddr.vaddr_bitmap, bit_idx_start + cnt++, 1);
        }

        vaddr_start = kernel_vaddr.vaddr_start + bit_idx_start * PG_SIZE;
    }
    else { }  // 用户内存池 

    return (void *)vaddr_start;

}


// 得到虚拟地址vaddr对应的pte指针
uint32_t *pte_ptr(uint32_t vaddr)
{
    uint32_t *pte = (uint32_t*)(0xffc00000 + ((vaddr & 0xffc00000) >> 10) + PTE_IDX(vaddr) * 4);
    return pte;
}


// 得到虚拟地址vaddr对应的pde指针
uint32_t *pde_ptr(uint32_t vaddr)
{
    uint32_t *pde = (uint32_t*)((0xfffff000) + PDE_IDX(vaddr) * 4);
    return pde;
}


// 在m_pool指向的物理内存池中分配1个物理页
static void *palloc(struct pool *m_pool)
{
    // 找到一个物理页
    int bit_idx = bitmap_scan(&m_pool->pool_bitmap, 1);
    if (bit_idx == -1)
    {
        return NULL;
    }

    // 将此位置1
    bitmap_set(&m_pool->pool_bitmap, bit_idx, 1);
    // uint32_t page_phyaddr = ((bit_idx * PG_SIZE) + m_pool->phy_addr_start);
    uint32_t page_phyaddr = m_pool->phy_addr_start + bit_idx * PG_SIZE;
    return (void *)page_phyaddr;
}


// 页表中添加虚拟地址_vaddr与物理地址_page_phyaddr的映射
static void page_table_add(void *_vaddr, void *_page_phyaddr)
{
    uint32_t vaddr = (uint32_t)_vaddr;
    uint32_t page_phyaddr = (uint32_t)_page_phyaddr;
    uint32_t *pde = pde_ptr(vaddr);
    uint32_t *pte = pte_ptr(vaddr);

    // 判断页目录项的p位,为1表示该表已存在
    if (*pde & 0x00000001)
    {  
        if(!(*pte & 0x00000001))
        {
            *pte = (page_phyaddr | PG_US_U | PG_RW_W | PG_P_1);
        }
        else
        {
          // pte repeat
        }
    }
    else
    {
        // 页目录项不存在,先创建页目录项,再创建页表项
        uint32_t pde_phyaddr = (uint32_t)palloc(&kernel_pool);
        *pde = (pde_phyaddr | PG_US_U | PG_RW_W | PG_P_1);
        memset((void*)((int)pte & 0xfffff000), 0, PG_SIZE);
        *pte = (page_phyaddr | PG_US_U | PG_RW_W | PG_P_1);
    }
}



// 分配pg_cnt个页空间,成功返回起始虚拟地址,失败返回NULL.
void *malloc_page(enum pool_flags pf, uint32_t pg_cnt)
{
    // 1 通过 vaddr_get 在虚拟内存池中申请虚拟地址
    // 2 通过 palloc 在物理内存池中申请物理页
    // 3 通过 page_table_add 将以上得到的虚拟地址和物理地址在页表中完成映射
    void *vaddr_start = vaddr_get(pf, pg_cnt);
    if (vaddr_start == NULL) {
        return NULL;
    }

    uint32_t vaddr = (uint32_t)vaddr_start;
    uint32_t cnt = pg_cnt;
    struct pool *mem_pool = pf & PF_KERNEL ? &kernel_pool : &user_pool;

    // 虚拟地址和物理地址逐个映射
    while (cnt-- > 0)
    {
        void *page_phyaddr = palloc(mem_pool);
        if (page_phyaddr == NULL)
        {
            return NULL;
        }
        page_table_add((void*)vaddr, page_phyaddr);
        vaddr += PG_SIZE;
    }

    return vaddr_start;
}


// 从内核物理内存池中申请1页内存,成功返回虚拟地址,失败返回NULL.
void *get_kernel_pages(uint32_t pg_cnt)
{
    void *vaddr = malloc_page(PF_KERNEL, pg_cnt);
    if (vaddr != NULL)
    {
        memset(vaddr, 0, pg_cnt * PG_SIZE);
    }

    return vaddr;
}


// 初始化内存池
static void mem_pool_init(uint32_t all_mem)
{
    put_str("   memory_init_start\n"); 

    // 计算数据
    uint32_t page_table_size = PG_SIZE * 256; // 到目前为止, 共创建了256个页表, 则页表占用的空间 = 4096 * 256 = 1M
    uint32_t used_mem = page_table_size + 0x100000; // 页表空间大小 + 低端1M内存
    uint32_t free_mem = all_mem - used_mem; // 32M - 2M = 30M
    uint16_t all_free_pages = free_mem / PG_SIZE; // 7680个

    uint16_t kernel_free_pages = all_free_pages / 2; // 用户和内核各分一半的可用内存, 各3840个
    uint16_t user_free_pages = all_free_pages - kernel_free_pages;
    uint32_t kbm_length = kernel_free_pages / 8;  // 计算表示kernel_free_pages个页需要多少个字节(需要3840 / 8 = 480个字节). 1位表示1页
    uint32_t ubm_length = user_free_pages / 8;    // 计算表示user_free_pages个页需要多少个字节(需要3840 / 8 = 480个字节). 1位表示1页
    uint32_t kp_start = used_mem; // 内核内存池起始物理地址
    uint32_t up_start = kp_start + kernel_free_pages * PG_SIZE; // 用户内存池起始物理地址


    // 初始化内核内存池和用户内存池位图
    kernel_pool.phy_addr_start = kp_start;
    user_pool.phy_addr_start = up_start;

    kernel_pool.pool_size = kernel_free_pages * PG_SIZE;
    user_pool.pool_size = user_free_pages * PG_SIZE;

    kernel_pool.pool_bitmap.btmp_bytes_len = kbm_length; // 所需字节个数
    user_pool.pool_bitmap.btmp_bytes_len = ubm_length;   // 所需字节个数

    kernel_pool.pool_bitmap.bits = (void*)MEM_BITMAP_BASE; // 位图所在的位置 0xc009a000
    user_pool.pool_bitmap.bits = (void*)(MEM_BITMAP_BASE + kbm_length);


    // 将位图置0
    bitmap_init(&kernel_pool.pool_bitmap);
    bitmap_init(&user_pool.pool_bitmap);


    // 输出内存池信息
    put_str("      [ kernel-pool-bitmap-start:  0x");
    put_int((int)kernel_pool.pool_bitmap.bits);
    put_str("\n");
    put_str("      kernel-pool-phy-addr-start:  0x00"); 
    put_int(kernel_pool.phy_addr_start); 
    put_str(" ]");
    put_str("\n");
    put_str("      [ user-pool-bitmap-start  :  0x"); 
    put_int((int)user_pool.pool_bitmap.bits);
    put_str("\n");
    put_str("      user-pool-phy-addr-start  :  0x0"); 
    put_int(user_pool.phy_addr_start); 
    put_str(" ]");
    put_str("\n");


    // 初始化内核虚拟地址位图
    kernel_vaddr.vaddr_bitmap.btmp_bytes_len = kbm_length;
    kernel_vaddr.vaddr_bitmap.bits = (void*)(MEM_BITMAP_BASE + kbm_length + ubm_length);
    kernel_vaddr.vaddr_start = K_HEAP_START; // 0xc0100000
    // 将位图置0
    bitmap_init(&kernel_vaddr.vaddr_bitmap);


    // 输出内存池信息
    put_str("      [ kernel-vaddr-bitmap-start: 0x");
    put_int((int)kernel_vaddr.vaddr_bitmap.bits);
    put_str("\n");
    put_str("      kernel-vaddr-vaddr-start:    0x"); 
    put_int(kernel_vaddr.vaddr_start); 
    put_str(" ]");
    put_str("\n\n");


    // 考虑内存对齐
    put_str("      kernel_pool vaddr  = 0x");
    put_int((uint32_t)(void *)&kernel_pool);
    put_str("\n");
    put_str("      user_pool vaddr    = 0x");
    put_int((uint32_t)(void *)&user_pool);
    put_str("\n");
    put_str("      kernel_vaddr vaddr = 0x");
    put_int((uint32_t)(void *)&kernel_vaddr);
    put_str("\n");


    put_str("   memory_init done\n\n");

}
  
// 初始化内存
void mem_init()
{

    // uint32_t mem_bytes_total = (*(uint32_t*)(0xb00));
    uint32_t mem_bytes_total = 32 * 1024 * 1024; // 假如物理内存32M
    mem_pool_init(mem_bytes_total);

}
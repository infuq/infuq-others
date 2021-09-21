#ifndef __KERNEL_MEMORY_H
#define __KERNEL_MEMORY_H
#include "stdint.h"
#include "bitmap.h"
#include "list.h"

enum pool_flags
{
    PF_KERNEL = 1,  // 内核内存池
    PF_USER = 2     // 用户内存池
};

#define PG_P_1  1    // 页表项或页目录项存在属性位
#define PG_P_0  0    // 页表项或页目录项存在属性位
#define PG_RW_R 0    // R/W 属性位值, 读/执行
#define PG_RW_W 2    // R/W 属性位值, 读/写/执行
#define PG_US_S 0    // U/S 属性位值, 系统级
#define PG_US_U 4    // U/S 属性位值, 用户级

// 虚拟地址池,用于虚拟地址管理
struct virtual_addr
{
    struct bitmap vaddr_bitmap;
    uint32_t vaddr_start;
};


void mem_init();


void *get_kernel_pages(unsigned int page_count);
void *malloc_page(enum pool_flags pf, unsigned int page_count);
void *get_a_page(enum pool_flags pf, unsigned int vaddr);

void *get_user_pages(unsigned int page_count);

unsigned int *pte_ptr(unsigned int vaddr);
unsigned int *pde_ptr(unsigned int vaddr);

unsigned int addr_v2p(unsigned int vaddr);




#endif

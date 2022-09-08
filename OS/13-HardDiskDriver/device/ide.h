#ifndef __DEVICE_IDE_H
#define __DEVICE_IDE_H
#include "stdint.h"
#include "sync.h"
#include "list.h"
#include "bitmap.h"

// ide_channel -> disk -> partition


/* 分区结构 */
struct partition {
   uint32_t start_lba;		 // 分区的起始扇区
   uint32_t sec_cnt;		    // 分区的扇区数
   struct disk* my_disk;	 // 分区所属的硬盘
   struct list_elem part_tag;	 // 用于队列中的标记
   char name[8];		          // 分区名称. 例如sda1,sda2

   // 以下与文件系统相关
   struct super_block* sb;	       // 本分区的超级块
   struct bitmap block_bitmap;	 // 块位图
   struct bitmap inode_bitmap;	 // i结点位图
   struct list open_inodes;	    // 本分区打开的i结点队列
};

/* 硬盘结构 */
struct disk {
   char name[8];			               // 硬盘名称,如sda,sdb
   struct ide_channel* my_channel;	   // 硬盘所在的通道,如ide0
   uint8_t dev_no;			            // 表示本硬盘是主盘(0)还是从盘(1)
   struct partition prim_parts[4];	   // 主分区数量,最多4个
   struct partition logic_parts[8];	   // 逻辑分区数量,虽然没有数量限制,但这里限制最多8个
};

/* ata或ide通道结构 */
struct ide_channel {
   char name[8];		       // 通道名称, 如ata0,也被叫做ide0. 可以参考bochs配置文件中关于硬盘的配置
   uint16_t port_base;		 // 本通道的起始端口号
   uint8_t irq_no;		    // 本通道所用的中断号
   struct lock lock;
   bool expecting_intr;		 // 向硬盘发完命令后等待来自硬盘的中断
   struct semaphore disk_done;	 // 硬盘处理完成.线程用这个信号量来阻塞自己,由硬盘完成后产生的中断将线程唤醒
   struct disk devices[2];	 // 一个通道上连接两个硬盘,一主一从
};

void intr_hd_handler(uint8_t irq_no);
void ide_init(void);
extern uint8_t channel_cnt;
extern struct ide_channel channels[];
extern struct list partition_list;
void ide_read(struct disk* hd, uint32_t lba, void* buf, uint32_t sec_cnt);
void ide_write(struct disk* hd, uint32_t lba, void* buf, uint32_t sec_cnt);


#endif

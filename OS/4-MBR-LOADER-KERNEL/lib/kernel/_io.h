/**
 * - CRT 地址寄存器 0x3D4
 * - CRT 数据寄存器 0x3D5
 * - CRT 光标位置 - 高位 0xE
 * - CRT 光标位置 - 低位 0xF
 * 
 */

#ifndef INFUQ_IO_H
#define INFUQ_IO_H

#include "_types.h"

// 读入一个字节
extern u8 inb(u16 port);
// 读入一个字
extern u16 inw(u16 port);


// 写入一个字节
extern void outb(u16 port, u8 value);
// 写入一个字
extern void outw(u16 port, u16 value);


#endif

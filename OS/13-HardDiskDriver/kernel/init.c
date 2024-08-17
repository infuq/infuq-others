#include "init.h"
#include "print.h"
#include "interrupt.h"
#include "memory.h"
#include "timer.h"
#include "thread.h"
#include "console.h"
#include "keyboard.h"
#include "tss.h"
#include "ide.h"


// 负责初始化所有模块
void init_all()
{
	put_str("invoke init_all\n");
	
	
	idt_init();				// 中断

	mem_init();				// 内存管理
	
	main_thread_init();		// 初始化main线程
   
   	timer_init();			// 时钟中断

	console_init();			// 初始化全局控制台锁
   	
   	keyboard_init();		// 键盘初始化
   	
   	tss_init();				// TSS初始化

	ide_init();	     		// 初始化硬盘


	
}
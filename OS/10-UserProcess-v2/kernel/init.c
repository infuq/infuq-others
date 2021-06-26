#include "init.h"
#include "print.h"
#include "interrupt.h"
#include "memory.h"
#include "timer.h"
#include "thread.h"
#include "sync.h"
#include "console.h"
#include "keyboard.h"
#include "tss.h"


// 负责初始化所有模块
void init_all()
{
	put_str("invoke init_all\n");
	
	// 中断
	idt_init();

	// 内存管理
	mem_init();

	// 初始化全局控制台锁
	console_init();

	// 初始化main线程
	main_thread_init();
   
   	timer_init();

   	// 键盘初始化
   	keyboard_init();

   	// TSS初始化
   	tss_init();
	
}
#include "init.h"
#include "print.h"
#include "interrupt.h"
#include "memory.h"
#include "timer.h"
#include "thread.h"

// 负责初始化所有模块
void init_all()
{
	put_str("invoke init_all\n");
	
	// 中断
	idt_init();

	// 内存管理
	mem_init();

	thread_init();
   
   	timer_init();
	
}
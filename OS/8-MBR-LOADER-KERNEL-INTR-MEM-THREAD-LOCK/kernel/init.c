#include "init.h"
#include "print.h"
#include "interrupt.h"
#include "memory.h"
#include "timer.h"
#include "thread.h"
#include "sync.h"

// 负责初始化所有模块
void init_all()
{
	put_str("invoke init_all\n");
	
	// 中断
	idt_init();

	// 内存管理
	mem_init();

	console_init();

	thread_init();
   
   	timer_init();
	
}
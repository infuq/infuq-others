#include "init.h"
#include "print.h"
#include "interrupt.h"

// 负责初始化所有模块
void init_all()
{
	put_str("invoke init_all\n");
	idt_init();
}
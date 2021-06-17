#include "print.h"
#include "init.h"

int main(void)
{
	put_str("invoke main[kernel init]\n");

	init_all();
	asm volatile("sti"); //开中断

	while(1);
	return 0;
}
#include "print.h"
#include "init.h"
#include "memory.h"

int main()
{
	put_str("invoke main[kernel init]\n");

	init_all();

	// 允许中断发生                  cli表示禁止中断发生
	asm volatile("sti");

	void *addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");

	while(1);
	
	return 0;

	
}
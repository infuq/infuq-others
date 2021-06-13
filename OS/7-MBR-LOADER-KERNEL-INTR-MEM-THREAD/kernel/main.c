#include "print.h"
#include "init.h"
#include "memory.h"
#include "thread.h"

void k_thread_a(void *);


int main(void)
{
	put_str("invoke main[kernel init]\n");

	init_all();

	// 允许中断发生                  cli表示禁止中断发生
	asm volatile("sti");

	void *addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");


    thread_start("k_thread_a", 31, k_thread_a, "argA");



	while (1);
	
	return 0;
}


void k_thread_a(void *arg)
{
	char *pArg = arg;
	int count = 3;
	while (count--)
	{
		put_str(pArg);
	}
}
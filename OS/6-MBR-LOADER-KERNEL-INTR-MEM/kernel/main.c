#include "print.h"
#include "init.h"

int main(void)
{
	put_str("invoke main[kernel init]\n");

	init_all();
	asm volatile("sti");

	void *addr = NULL;
	addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");

	while(1);
	
	return 0;
}
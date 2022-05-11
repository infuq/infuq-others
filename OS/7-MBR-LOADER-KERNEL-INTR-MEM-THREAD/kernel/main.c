#include "print.h"
#include "init.h"
#include "memory.h"
#include "thread.h"
#include "interrupt.h"

void k_thread_1(void *);
void k_thread_2(void *);


int main(void)
{
	put_str("invoke main[kernel init]\n");

	init_all();


	void *addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");


    struct task_struct *thread1 = thread_start("k_thread_1", 10, k_thread_1, "[thread_1 ]");
    struct task_struct *thread2 = thread_start("k_thread_2", 16, k_thread_2, "[thread_2 ]");
    // 打印PCB地址
    put_str("thread1 vaddr = 0x");
    put_int((uint32_t)(void *)thread1);
    put_str("\n");
    put_str("thread2 vaddr = 0x");
    put_int((uint32_t)(void *)thread2);
    put_str("\n\n");

    intr_enable();


    // https://gitee.com/infuq/infuq-img/blob/master/img/Snipaste_2021-06-18_08-00-38.png
	while (1)
	{
		put_str("[thread_main ]");
	}

	return 0;
}


void k_thread_1(void *arg)
{
	char *pArg = arg;
	while (1)
	{
		put_str(pArg);
	}
}
void k_thread_2(void *arg)
{
	char *pArg = arg;
	while (1)
	{
		put_str(pArg);
	}
}
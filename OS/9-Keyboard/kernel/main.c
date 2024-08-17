#include "print.h"
#include "init.h"
#include "memory.h"
#include "thread.h"
#include "interrupt.h"
#include "sync.h"
#include "console.h"
#include "ioqueue.h"
#include "keyboard.h"

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

    

	while (1);/*
	{
		console_put_str("[thread_main ]");
	}
*/
	return 0;
}




void k_thread_1(void *arg)
{

	char *pArg = arg;
	while (1)
	{
		enum intr_status old_status = intr_disable();
		if (!ioq_empty(&kbd_buf))
		{
			console_put_str(pArg);
			char byte = ioq_getchar(&kbd_buf);
			console_put_char(byte);
			console_put_str("\n");
		}
		intr_set_status(old_status);
	}
	

}


void k_thread_2(void *arg)
{

	char *pArg = arg;
	
	while (1)
	{
		enum intr_status old_status = intr_disable();
		if (!ioq_empty(&kbd_buf))
		{
			console_put_str(pArg);
			char byte = ioq_getchar(&kbd_buf);
			console_put_char(byte);
			console_put_str("\n");
		}
		intr_set_status(old_status);
	}


}


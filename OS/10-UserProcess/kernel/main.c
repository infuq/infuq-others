#include "print.h"
#include "init.h"
#include "memory.h"
#include "thread.h"
#include "interrupt.h"
#include "sync.h"
#include "console.h"
#include "ioqueue.h"
#include "keyboard.h"
#include "process.h"


void k_thread_1(void *);
void k_thread_2(void *);

void u_process_1();
void u_process_2();

int var_1 = 0;
int var_2 = 0;

int main()
{
	put_str("invoke main[kernel init]\n");

	init_all();

	

	void *addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");


    // 创建内核线程, 加入到队列中, 等待时钟中断调用它
    struct task_struct *thread1 = thread_start("k_thread_1", 10, k_thread_1, "[k_thread_1 ]");
    struct task_struct *thread2 = thread_start("k_thread_2", 3, k_thread_2, "[k_thread_2 ]");
    // 打印PCB地址
    //put_str("thread1 vaddr = 0x");
    //put_int((uint32_t)(void *)thread1);
    //put_str("\n");
    //put_str("thread2 vaddr = 0x");
    //put_int((uint32_t)(void *)thread2);
    //put_str("\n\n");

    
    // 创建用户进程, 加入到队列中, 等待时钟中断调用它
    // 当时钟中断调用到用户进程时, 用户进程首先在内核态执行, 会向中断栈(intr_stack)中存储CS的RPL=3, 当中断返回时, 就会进入用户态 
    //process_execute(u_process_1, "[u_process_1 ]");
    //process_execute(u_process_2, "[u_process_2 ]");

	intr_enable();
    

	while (1);

	return 0;
}

void u_process_1()
{
}

void u_process_2()
{

	while (1)
	{
		var_2++;
	}
}


void k_thread_1(void *arg)
{
	int i = 3;
	while (i-- > 0)
	{
		console_put_str("k_thread_1 i=");
		console_put_int(i);
		console_put_str("\n");
	}

}


void k_thread_2(void *arg)
{

	int j = 3;
	while (j-- > 0)
	{
		console_put_str("k_thread_2 j=");
		console_put_int(j);
		console_put_str("\n");
	}

}

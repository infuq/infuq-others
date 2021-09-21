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
#include "syscall-init.h"
#include "syscall.h"


void k_thread_1(void *);
void k_thread_2(void *);

void u_process_1();
void u_process_2();

int prog_1_pid = 0;
int prog_2_pid = 0;


int main()
{
	put_str("invoke main[kernel init]\n");

	init_all();

	

	void *addr = get_kernel_pages(3);
	put_str("\nget_kernel_pages start vaddr = 0x");
    put_int((uint32_t)addr);
    put_str("\n\n");


    process_execute(u_process_1, "[u_process_1 ]");
    process_execute(u_process_2, "[u_process_2 ]");



    struct task_struct *thread1 = thread_start("k_thread_1", 10, k_thread_1, "[k_thread_1 ]");
    struct task_struct *thread2 = thread_start("k_thread_2", 16, k_thread_2, "[k_thread_2 ]");
    // 打印PCB地址
    put_str("thread1 vaddr = 0x");
    put_int((uint32_t)(void *)thread1);
    put_str("\n");
    put_str("thread2 vaddr = 0x");
    put_int((uint32_t)(void *)thread2);
    put_str("\n\n");

    

    
	intr_enable();
    

	while (1);

	return 0;
}

void u_process_1()
{
	prog_1_pid = getpid();
	while (1);

}

void u_process_2()
{
	prog_2_pid = getpid();
	while (1);

}


void k_thread_1(void *arg)
{

	char *pArg = arg;
	
	while (1)
	{
		console_put_str(pArg);
		console_put_int(sys_getpid());
		console_put_str(" : ");
		console_put_int(prog_1_pid);
		console_put_str("\n");
	}

}


void k_thread_2(void *arg)
{

	char *pArg = arg;
	
	while (1)
	{
		console_put_str(pArg);
		console_put_int(sys_getpid());
		console_put_str(" : ");
		console_put_int(prog_2_pid);
		console_put_str("\n");
	}

}
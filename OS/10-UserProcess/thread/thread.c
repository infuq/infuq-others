#include "thread.h"
#include "stdint.h"
#include "string.h"
#include "global.h"
#include "memory.h"
#include "list.h"
#include "print.h"
#include "interrupt.h"
#include "process.h"
#include "debug.h"
#include "console.h"


struct task_struct *main_thread;    // 主线程 PCB
struct list thread_ready_list;      // 就绪队列
struct list thread_all_list;        // 所有任务队列
static struct list_elem *thread_tag; // 用于保存队列中的线程结点
extern void switch_to(struct task_struct *cur, struct task_struct *next);


struct task_struct *running_thread()
{
    uint32_t esp;
    asm ("mov %%esp, %0" : "=g" (esp));
    // 返回esp整数部分,即PCB起始地址
    return (struct task_struct *)(esp & 0xfffff000);
}


// 由 kernel_thread 去执行 func(arg)
static void kernel_thread(thread_func *func, void *arg)
{

    /* 执行func之前要开中断,避免后面的时钟中断被屏蔽,而无法调度其它线程 */
    intr_enable();

    func(arg);

}


// 初始化线程栈
void thread_create(struct task_struct *pthread, thread_func function, void *func_arg)
{
    // 中断栈空间
    pthread->self_kstack -= sizeof(struct intr_stack);
    
    // 线程栈空间
    pthread->self_kstack -= sizeof(struct thread_stack);
    struct thread_stack *kthread_stack = (struct thread_stack *)pthread->self_kstack;
    kthread_stack->eip = kernel_thread;
    kthread_stack->function = function;
    kthread_stack->func_arg = func_arg;
    kthread_stack->ebp = kthread_stack->ebx = kthread_stack->esi = kthread_stack->edi = 0;
}


// 初始化线程基本信息
void init_thread(struct task_struct *pthread, char *name, int priority)
{
    memset(pthread, 0, sizeof(*pthread));
    strcpy(pthread->name, name);
    
    if (pthread == main_thread)
        pthread->status = TASK_RUNNING;
    else
        pthread->status = TASK_READY;

    
    // 线程在内核态下使用的栈顶地址
    pthread->self_kstack        = (uint32_t*)((uint32_t)pthread + PG_SIZE);
    pthread->priority           = priority;
    pthread->ticks              = priority;
    pthread->elapsed_ticks      = 0;
    pthread->pgdir              = NULL;
    pthread->stack_magic        = 0x19900210; // 自定义魔数
}


// 创建线程
struct task_struct *thread_start(char *name, int prio, thread_func func, void *arg)
{
    // 所有PCB都位于内核空间(包括用户进程的PCB)
    struct task_struct *thread = get_kernel_pages(1);

    init_thread(thread, name, prio);
    thread_create(thread, func, arg);

    /* 确保之前不在队列中 */
    ASSERT(!elem_find(&thread_ready_list, &thread->general_tag));
    /* 加入就绪线程队列 */
    list_append(&thread_ready_list, &thread->general_tag);

    /* 确保之前不在队列中 */
    ASSERT(!elem_find(&thread_all_list, &thread->all_list_tag));
    /* 加入全部线程队列 */
    list_append(&thread_all_list, &thread->all_list_tag);
    
    return thread;
}


static void make_main_thread()
{
    main_thread = running_thread();
    init_thread(main_thread, "main", 31);

    /* main函数是当前线程,当前线程不在thread_ready_list中,
    * 所以只将其加在thread_all_list中. */
    ASSERT(!elem_find(&thread_all_list, &main_thread->all_list_tag));
    list_append(&thread_all_list, &main_thread->all_list_tag);
}



/* 实现任务调度 */
void schedule()
{

    
    ASSERT(intr_get_status() == INTR_OFF);

    struct task_struct *cur = running_thread();


    if (cur->status == TASK_RUNNING) // 若此线程只是CPU时间片到了,将其加入到就绪队列尾
    {

        ASSERT(!elem_find(&thread_ready_list, &cur->general_tag));
        list_append(&thread_ready_list, &cur->general_tag);
        cur->ticks = cur->priority;     // 重新将当前线程的ticks再重置为其priority;
        cur->status = TASK_READY;
    }
    else
    {
        /* 若此线程需要某事件发生后才能继续上CPU运行,不需要将其加入队列,因为当前线程不在就绪队列中 */
    }

    ASSERT(!list_empty(&thread_ready_list));
    thread_tag = NULL;     // thread_tag清空
    thread_tag = list_pop(&thread_ready_list);    /* 将thread_ready_list队列中的第一个就绪线程弹出,准备将其调度上CPU. */
    struct task_struct *next = elem2entry(struct task_struct, general_tag, thread_tag);
    next->status = TASK_RUNNING;

    

    // 激活任务页表等
    process_activate(next);


    switch_to(cur, next);

}



/* 初始化main线程环境 */
void main_thread_init()
{
    put_str("\nthread_init start\n");

    list_init(&thread_ready_list);
    list_init(&thread_all_list);
    
    /* 将当前main函数创建为线程 */
    make_main_thread();

    put_str("thread_init done\n");
}



// 当前线程将自己阻塞,标志其状态为 stat(取值必须为 BLOCKED WAITING HANGING 之一)
void thread_block(enum task_status stat)
{
    enum intr_status old_status = intr_disable();
    struct task_struct *cur_thread = running_thread();
    cur_thread->status = stat;
    
    schedule();
    
    intr_set_status(old_status);
}

// 解除阻塞
void thread_unblock(struct task_struct *pthread)
{
    enum intr_status old_status = intr_disable();
    if (pthread->status != TASK_READY)
    {
        if (elem_find(&thread_ready_list, &pthread->general_tag))
        {
            // 错误! blocked thread in ready_list
        }
        // 放到队列的最前面,使其尽快得到调度
        list_push(&thread_ready_list, &pthread->general_tag);
        pthread->status = TASK_READY;
    }

    intr_set_status(old_status);

}

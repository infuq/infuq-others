#ifndef __USERPROG_PROCESS_H 
#define __USERPROG_PROCESS_H

#include "thread.h"
#include "stdint.h"

#define default_prio 3
#define USER_STACK3_VADDR  (0xc0000000 - 0x1000)
#define USER_VADDR_START 0x8048000

void process_execute(void *func, char *name);
void process_activate(struct task_struct *p_thread);

#endif

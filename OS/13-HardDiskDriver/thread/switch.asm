[bits 32]
section .text
global switch_to

; 调用 switch_to(cur, next)

switch_to:
    ; next
    ; cur
    ; 栈中此处是返回地址
    push esi
    push edi
    push ebx
    push ebp

    mov eax, [esp + 20]     ; 得到栈中的参数cur, cur = [esp + 20]
    mov [eax], esp          ; 保存栈顶指针esp. task_struct的self_kstack字段,
                            ; self_kstack在task_struct中的偏移为0,
                            ; 所以直接往thread开头处存4字节便可.

    ; 以上操作的是当前线程的内核线程栈, esp值被保存到cur->self_kstack


;------------------  上面是备份当前线程的环境,下面是恢复下一个线程的环境  ----------------
   mov eax, [esp + 24]      ; 得到栈中的参数next, next = [esp + 24]
   mov esp, [eax]           ; PCB的第一个成员是self_kstack成员,用来记录0级栈顶指针,
                            ; 用来上CPU时恢复0级栈,0级栈中保存了进程或线程所有信息,包括3级栈指针
   
   ; 上面两个mov操作之后, esp指向next线程的内核线程栈的栈顶

   pop ebp
   pop ebx
   pop edi
   pop esi
   ret                      ; 返回到上面switch_to下面的那句注释的返回地址,
                            ; 未由中断进入,第一次执行时会返回到kernel_thread

                            ; ret 将栈顶的4字节数据弹出到寄存器eip, 同时esp自加4





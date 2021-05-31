[bits 32]
%define ERROR_CODE nop
%define ZERO push 0

extern idt_table

section .data
global intr_entry_table
intr_entry_table:

%macro VECTOR 2
    section .text
    intr%1entry:
        %2
        push ds
        push es
        push fs
        push gs
        pushad
        
        ;如果是从片上进入到中断,除了往从片上发送EOI外,还要往主片上发送EOI
        mov al,0x20
        out 0xa0,al
        out 0x20,al
        
        push %1
        call [idt_table + %1*4]
        jmp intr_exit
        
    section .data
        dd intr%1entry
%endmacro

section .text
global intr_exit
intr_exit:
    add esp,4
    popad
    pop gs
    pop fs
    pop es
    pop ds
    add esp,4
    iretd

VECTOR 0X00,ZERO
VECTOR 0X01,ZERO
VECTOR 0X02,ZERO
VECTOR 0X03,ZERO
VECTOR 0X04,ZERO
VECTOR 0X05,ZERO
VECTOR 0X06,ZERO
VECTOR 0X07,ZERO
VECTOR 0X08,ZERO
VECTOR 0X09,ZERO
VECTOR 0X0a,ZERO
VECTOR 0X0b,ZERO
VECTOR 0X0c,ZERO
VECTOR 0X0d,ZERO
VECTOR 0X0e,ZERO
VECTOR 0X0f,ZERO
VECTOR 0X10,ZERO
VECTOR 0X11,ZERO
VECTOR 0X12,ZERO
VECTOR 0X13,ZERO
VECTOR 0X14,ZERO
VECTOR 0X15,ZERO
VECTOR 0X16,ZERO
VECTOR 0X17,ZERO
VECTOR 0X18,ZERO
VECTOR 0X19,ZERO
VECTOR 0X1a,ZERO
VECTOR 0X1b,ZERO
VECTOR 0X1c,ZERO
VECTOR 0X1d,ZERO
VECTOR 0X1e,ERROR_CODE
VECTOR 0X1f,ZERO
VECTOR 0X20,ZERO


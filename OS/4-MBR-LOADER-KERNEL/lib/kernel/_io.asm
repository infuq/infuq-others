TI_GDT 	equ 0
RPL0 	equ 0
SELECTOR_VIDEO equ (0x0003<<3)+TI_GDT+RPL0



[bits 32]

section .text

global inb
inb:
    push ebp
    mov ebp, esp

    xor eax, eax
    mov edx, [ebp + 8]
    in al, dx

    jmp $+2; 一点点延迟
    jmp $+2
    jmp $+2

    leave
    ret


global outb
outb:
    push ebp
    mov ebp, esp

    mov ax,SELECTOR_VIDEO
	mov gs,ax

    mov edx, [ebp + 8]; 入参port
    mov eax, [ebp + 12]; 入参value
    out dx, al

    jmp $+2
    jmp $+2
    jmp $+2

    leave
    ret



global inw
inw:
    push ebp
    mov ebp, esp

    xor eax, eax
    mov edx, [ebp + 8]
    in ax, dx

    jmp $+2; 一点点延迟
    jmp $+2
    jmp $+2

    leave
    ret


global outw
outw:
    push ebp
    mov ebp, esp

    mov ax,SELECTOR_VIDEO
	mov gs,ax

    mov edx, [ebp + 8]; 入参port
    mov eax, [ebp + 12]; 入参value
    out dx, ax

    jmp $+2
    jmp $+2
    jmp $+2

    leave
    ret    
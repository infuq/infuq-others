%include "boot.inc"
SECTION LOADER vstart=LOADER_BASE_ADDR

jmp protect_mode

gdt:
;0描述符
	dd	0x00000000
	dd	0x00000000
;1描述符(4GB代码段描述符)
	dd	0x0000ffff
	dd	0x00cf9800
;2描述符(4GB数据段描述符)
	dd	0x0000ffff
	dd	0x00cf9200
;3描述符(28Kb的视频段描述符)
	dd	0x80000007
	dd	0x00c0920b

lgdt_value:
	dw $-gdt-1	;高16位表示表的最后一个字节的偏移（表的大小-1） 
	dd gdt		;低32位表示起始位置（GDT的物理地址）

SELECTOR_CODE	equ	0x0001<<3
SELECTOR_DATA	equ	0x0002<<3
SELECTOR_VIDEO	equ	0x0003<<3

protect_mode:
;进入32位
	lgdt [lgdt_value]
	in al,0x92
	or al,0000_0010b
	out 0x92,al
	cli
	mov eax,cr0
	or eax,1
	mov cr0,eax
	
	jmp dword SELECTOR_CODE:main
	
[bits 32]
;正式进入32位
main:
mov ax,SELECTOR_DATA
mov ds,ax
mov es,ax
mov ss,ax
mov esp,LOADER_STACK_TOP
mov ax,SELECTOR_VIDEO
mov gs,ax

mov byte [gs:0xa0],'3'
mov byte [gs:0xa2],'2'
mov byte [gs:0xa4],'m'
mov byte [gs:0xa6],'o'
mov byte [gs:0xa8],'d'

jmp $
%include "boot.inc"
SECTION LOADER vstart=0x900


; gdt占32个字节
gdt:
	;0描述符
	dd	0x00000000
	dd	0x00000000
	;1描述符(4GB代码段描述符) 段基址=0x0 段界限单位=4K 段界限=0xfffff 段范围=4K * 0xfffff = 4GB
	dd	0x0000ffff ; 低32位 00000000 00000000 11111111 11111111
	dd	0x00cf9800 ; 高32位 00000000 11001111 10011000 00000000
	;2描述符(4GB数据段描述符) 段基址=0x0 段界限单位=4K 段界限=0xfffff  段范围=4K * 0xfffff = 4GB
	dd	0x0000ffff ; 低32位 00000000 00000000 11111111 11111111
	dd	0x00cf9200 ; 高32位 00000000 11001111 10010010 00000000
	;3描述符(28Kb的视频段描述符) 段基址=0x000b8000 段界限单位=4K 段界限=0x00007 段范围=4K * 0x00007 = 28Kb
	dd	0x80000007 ; 低32位 10000000 00000000 00000000 00000111
	dd	0x00c0920b ; 高32位 00000000 11000000 10010010 00001011

; lgdt_value占6个字节 
lgdt_value:
	dw $-gdt-1	;低16位表示表的最后一个字节的偏移(表的大小-1)
				;dw 表示定义2个字节
	dd gdt		;高32位表示起始位置(GDT的物理地址)
				;dd 表示定义4个字节

; 不占字节
SELECTOR_CODE	equ	0x0001<<3	;SELECTOR_CODE = 8      每个描述符占用8字节,第0个描述符不使用,则代码段的描述符(即第1个描述符)需偏移8个字节
SELECTOR_DATA	equ	0x0002<<3	;SELECTOR_DATA = 16    每个描述符占用8字节,第0个描述符不使用,则数据段的描述符(即第2个描述符)需偏移16个字节
SELECTOR_VIDEO	equ	0x0003<<3 	;SELECTOR_VIDEO = 24    每个描述符占用8字节,第0个描述符不使用,则显存段的描述符(即第3个描述符)需偏移24个字节


; 以上共计 = 32 + 6 = 38 = 0x26 , 所以protect_mode的地址 = 0x900 + 0x26 = 0x926
protect_mode:
;进入32位
	; 加载GDT
	lgdt [lgdt_value]
	; 打开A20
	in al,0x92
	or al,0000_0010b
	out 0x92,al
	cli
	; cr0第0位置1
	mov eax,cr0
	or eax,0x00000001
	mov cr0,eax
	
	jmp dword SELECTOR_CODE:main 	; 刷新流水线
	
[bits 32]
;正式进入32位
main:
; 使用选择子初始化各段寄存器
mov ax,SELECTOR_DATA
mov ds,ax
mov es,ax
mov ss,ax
mov esp,LOADER_STACK_TOP
mov ax,SELECTOR_VIDEO
mov gs,ax

mov byte [gs:0xa0],'P'
mov byte [gs:0xa2],'r'
mov byte [gs:0xa4],'o'
mov byte [gs:0xa6],'t'
mov byte [gs:0xa8],'e'
mov byte [gs:0xaa],'c'
mov byte [gs:0xac],'t'
mov byte [gs:0xb0],'O'
mov byte [gs:0xb2],'N'
mov byte [gs:0xb4],'('
mov byte [gs:0xb6],'3'
mov byte [gs:0xb8],'2'
mov byte [gs:0xba],'M'
mov byte [gs:0xbc],'O'
mov byte [gs:0xbe],'D'
mov byte [gs:0xc0],')'

jmp $
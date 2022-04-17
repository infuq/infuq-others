%include "boot.inc"
; LOADER_BASE_ADDR equ 0x900
SECTION LOADER vstart=LOADER_BASE_ADDR

; 全局描述符表. 定义了4个段描述符,共占32个字节
gdt:
	;第0描述符
	;dd 表示定义4个字节
	;每个段描述符大小是8字节
	dd	0x00000000
	dd	0x00000000
	;第1描述符(4GB代码段描述符) 段基址=0x0 段界限单位=4K 段界限=0xfffff 段范围=4K * 0xfffff = 4GB
	dd	0x0000ffff ; 低32位 00000000 00000000 11111111 11111111
	dd	0x00cf9800 ; 高32位 00000000 11001111 10011000 00000000
	;第2描述符(4GB数据段描述符) 段基址=0x0 段界限单位=4K 段界限=0xfffff  段范围=4K * 0xfffff = 4GB
	dd	0x0000ffff ; 低32位 00000000 00000000 11111111 11111111
	dd	0x00cf9200 ; 高32位 00000000 11001111 10010010 00000000
	;第3描述符(28Kb的视频段描述符) 段基址=0x000b8000 段界限单位=4K 段界限=0x00007 段范围=4K * 0x00007 = 28Kb
	dd	0x80000007 ; 低32位 10000000 00000000 00000000 00000111
	dd	0x00c0920b ; 高32位 00000000 11000000 10010010 00001011


; gdtr_value占6个字节, 这6个字节的内容会被加载到GDTR寄存器
gdtr_value:
	dw	$-gdt-1	;低16位存储GDT的界限
				;dw 表示定义2个字节
	dd	gdt		;高32位表示起始位置(GDT的物理地址)
				;dd 表示定义4个字节


; 不占用字节空间
; 选择子
SELECTOR_CODE	equ	0x0001<<3	;SELECTOR_CODE = 8      每个描述符占用8字节,第0个描述符不使用,则代码段的描述符(即第1个描述符)需偏移8个字节
SELECTOR_DATA	equ	0x0002<<3	;SELECTOR_DATA = 16    	每个描述符占用8字节,第0个描述符不使用,则数据段的描述符(即第2个描述符)需偏移16个字节
SELECTOR_VIDEO	equ	0x0003<<3 	;SELECTOR_VIDEO = 24    每个描述符占用8字节,第0个描述符不使用,则显存段的描述符(即第3个描述符)需偏移24个字节


; 以上共计 = 32 + 6 = 38 = 0x26字节 , 所以在mbr.asm文件的41行 = 0x900 + 0x26 = 0x926
protected_mode:
; 准备进入32位

	cli; disable interrupts

	lgdt [gdtr_value]; load GDT register with start address of Global Descriptor Table

	in al, 0x92
	or al, 0000_0010b; Enable the A20 Line. 
	out 0x92, al

	mov eax, cr0
	or al, 1; set PE (Protection Enable) bit in CR0 (Control Register 0)
	mov cr0, eax

	
	jmp dword SELECTOR_CODE:main 	; 刷新流水线
									; 根据选择子SELECTOR_CODE从全局描述符表中找出对应的段描述符
	
[bits 32]
; 正式进入32位
main:
	mov ax,SELECTOR_DATA
	mov ds,ax
	mov es,ax
	mov fs,ax
	mov ss,ax
	mov esp,LOADER_STACK_TOP; 栈顶0x900
	mov ax,SELECTOR_VIDEO
	mov gs,ax

	; 保护模式(分段机制)下打印
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


	; 以上代码中, `段基址+偏移地址`得到真实物理地址.


	; 1.创建页表并初始化(页目录和页表)
	PAGE_DIR_TABLE_POS equ 0x100000 		; 页目录表放在物理地址0x100000处, 即紧挨着低端1M内存
	call setup_page

	; 2.页目录表起始地址存入 cr3 寄存器
	mov eax,PAGE_DIR_TABLE_POS
	mov cr3,eax

	; 3.cr0第31位(PG)置1
	mov eax,cr0
	or eax,0x80000000
	mov cr0,eax

	; 4.重新设置DGT并重新加载
	sgdt [gdtr_value]
	mov ebx,[gdtr_value + 2]              			; gdtr_value + 2个字节 表示得到GDT的起始物理地址, 即ebx存储GDT的起始物理地址
	or dword [ebx + 0x18 + 4],0xc0000000         	; ebx + 0x18(24个字节) 表示得到视频段的起始地址. 
												 	; 再加4个字节,则表示取最高32位,       0xc00 指向第768项
	add dword [gdtr_value + 2],0xc0000000			; GDTR寄存器中存储的是虚拟地址		
	add esp,0xc0000000							 	; 栈

	lgdt [gdtr_value]


	jmp dword SELECTOR_CODE:main0 					; 刷新流水线
													; 根据选择子SELECTOR_CODE从全局描述符表中找出对应的段描述符

main0:
	; 保护模式(分页机制)下打印
	mov byte [gs:0x1e0],'P'
	mov byte [gs:0x1e2],'A'
	mov byte [gs:0x1e4],'G'
	mov byte [gs:0x1e6],'E'
	mov byte [gs:0x1ea],'O'
	mov byte [gs:0x1ec],'N'
	mov byte [gs:0x1ee],'.'
	mov byte [gs:0x1f0],'.'
	mov byte [gs:0x1f2],'.'

	jmp $




setup_page:
	;先把页目录占用的空间(4K)逐字清零
	mov ecx,4096 		; 1024项,每项4字节, 共计 1024 * 4 = 4096 字节
	mov esi,0
.clear_page_dir:
	mov byte [PAGE_DIR_TABLE_POS + esi],0
	inc esi
	loop .clear_page_dir ; 每循环一次, ecx - 1
	
;开始创建页目录项(PDE)
.create_pde:
	mov eax,PAGE_DIR_TABLE_POS    ; 0x100000
	add eax,0x1000
	mov ebx,eax 		; ebx = 0x101000 作为第一个页表的位置及属性
	
	add eax,0x00000007 	; 或者 or eax,111b   即 eax = 0x101007					
	mov [PAGE_DIR_TABLE_POS + 0x0],eax		; 即第1个页目录项存储第一个页表的地址
	mov [PAGE_DIR_TABLE_POS + 0xc00],eax	; 0xc00 = 3072 , 每项4字节 , 则 3072 / 4 = 768
											; 即第768个页目录项存储第一个页表的地址
	sub eax,0x1000
	mov [PAGE_DIR_TABLE_POS + 4 * 1023],eax

;开始创建第一个页表的页表项(PTE)   每个页表有1024个页表项,此处只创建256个页表项(对应低端1M内存)
	mov ecx,256
	mov esi,0
	mov edx,111b
.create_pte:	; 此循环功能: 将低端1M内存分成256份,每份4K,每份的首地址逐个填充到第一个页表的0-256的页表项内
	mov [ebx + esi * 4],edx 		; ebx = 0x101000 是第一个页表的位置及属性
									; 每个页表项占用4个字节, 所以 esi * 4, esi从0开始递增
	add edx, 0x1000					; 0x1000 = 4K
	inc esi							; esi + 1, 即下次循环会指向第一个页表的下一个页表项
	loop .create_pte
	
;创建内核其他页表(769-1022项)的页目录项(PDE)       此段具体含义可以参考infuq-others\OS\创建页目录和页表.png 第一张图
	mov eax,PAGE_DIR_TABLE_POS
	add eax,0x2000                ; 指向第2个页表
	or eax,111b
	mov ebx,PAGE_DIR_TABLE_POS
	mov ecx,254               ; 共循环 1022 - 768 = 254 次
	mov esi,769
.create_kernel_pde:
	mov [ebx + esi * 4],eax
	inc esi
	add eax,0x1000
	loop .create_kernel_pde
	ret
TI_GDT 	equ 0
RPL0 	equ 0
SELECTOR_VIDEO equ (0x0003<<3) + TI_GDT + RPL0

[bits 32]
section .text



global put_str
put_str:	
	; 接下来的程序需要用到ebx和ecx, 因此需要先把ebx和ecx压栈
	push ebx
	push ecx

	xor ecx, ecx
	mov ebx, [esp + 12] ; [栈底,...,入参,调用方返回地址,ebx,ecx] 因此为了得到入参, 需要 +12个字节
.goon:
	mov cl, [ebx]
	cmp cl, 0
	jz .str_over 	; 如果读取到的字符是0, 则方法结束
	push ecx		; [栈底,...,入参,调用方返回地址,ebx,ecx,ecx]
	call put_char	; [栈底,...,入参,调用方返回地址,ebx,ecx,put_char入参,返回地址]
	add esp,4
	inc ebx
	jmp .goon
.str_over:
	pop ecx
	pop ebx
	ret





global put_char
put_char:

	; 将 EAX,ECX,EDX,EBX,ESP,EBP,ESI,EDI 压栈, 共 8个 * 每个4字节 = 32字节
	; [栈底,...,入参,调用方返回地址,ebx,ecx,put_char入参,返回地址(4字节),32个字节]
	pushad

	mov ax, SELECTOR_VIDEO
	mov gs, ax
	
	; 获取当前光标位置
	; 获得高8位
	mov dx, 0x03d4	; 索引寄存器
	mov al, 0x0e
	out dx, al
	mov dx, 0x03d5
	in al, dx
	mov ah, al
	
	; 获得低8位
	mov dx,0x03d4
	mov al,0x0f
	out dx,al
	mov dx,0x03d5
	in al,dx
	
	; 将光标存入bx
	mov bx, ax
	
	mov ecx, [esp + 36] ; 获取 put_char入参 
	
	cmp cl,0xd
	jz .is_carriage_return
	cmp cl,0xa
	jz .is_line_feed	
	cmp cl,0x8
	jz .is_backspace

	jmp .put_other
	
.is_backspace:
	dec bx
	shl bx,1
	mov byte [gs:bx],0x20
	inc bx
	mov byte [gs:bx],0x07
	shr bx,1
	jmp .set_cursor
	
.put_other:
	shl bx,1
	mov [gs:bx],cl
	inc bx
	mov byte [gs:bx],0x07
	shr bx,1
	inc bx
	cmp bx,2000
	jl .set_cursor
	
.is_line_feed:
.is_carriage_return:
;cr(\r)，只要把光标移到首行就行了
	xor dx,dx
	mov ax,bx
	mov si,80
	div si
	sub bx,dx
	
.is_carriage_return_end:
	add bx,80
	cmp bx,2000
.is_line_feed_end:
	jl .set_cursor
	
.roll_screen:
	cld
	mov ecx,960
	mov esi,0xc00b80a0	;第1行行首
	mov edi,0xc00b8000	;第0行行首
	rep movsd
	
	;最后一行填充为空白
	mov ebx,3840
	mov ecx,80
.cls:
	mov word [gs:ebx],0x0720
	add ebx,2
	loop .cls
	mov bx,1920	;最后一行行首
	
.set_cursor:
;将光标设为bx值
	;设置高8位
	mov dx,0x03d4
	mov al,0x0e
	out dx,al
	mov dx,0x03d5
	mov al,bh
	out dx,al
	
	;再设置低8位
	mov dx,0x03d4
	mov al,0x0f
	out dx,al
	mov dx,0x03d5
	mov al,bl
	out dx,al
.put_char_done:
	popad
	ret
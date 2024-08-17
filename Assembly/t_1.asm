assume cs:codeseg,ds:dataseg,ss:stackseg

; 功能: 将数据段中的'Hi Word'数据拷贝到栈

;
stackseg segment stack
	; dw	0,0,0,0,0,0,0,0
	dw 8 dup (0)
stackseg ends

;
dataseg segment
	dw ' d','ro','W ','iH'
	; db  dw  dd
dataseg ends

;
codeseg segment
start:
	; 设置栈段
	mov ax,stackseg
	mov ss,ax
	mov sp,10H
	; 设置数据段
	mov ax,dataseg
	mov ds,ax
	mov bx,0
	
	mov cx,4
move:	
	push ds:[bx]
	add bx,2
	loop move

	
	mov ax,4c00h
	int 21h	

codeseg ends

end start

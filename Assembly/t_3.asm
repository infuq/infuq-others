assume cs:codesg,ds:datasg,ss:stacksg

; 向屏幕中间打印数据段中的数据'Welcome to OS!'

datasg segment
	db 'Welcome to OS!'
datasg ends

stacksg segment stack
	db 8 dup (0)
stacksg ends

codesg segment
start:
	; 初始化数据段
	mov ax,datasg
	mov ds,ax
	mov si,0
	; 初始化附加段
	mov ax,0B800H
	mov es,ax
	mov di,160*12+80-16
	
	mov cx,14
print:
	mov al,ds:[si]
	mov es:[di],al
	mov al,70H
	mov es:[di+1],al
	inc si
	add di,2
	loop print
	
	mov ax,4C00H
	int 21H
codesg ends
end start


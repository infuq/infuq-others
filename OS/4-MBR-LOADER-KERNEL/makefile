
CFLAGS:= -m32
CFLAGS+= -Qn 						# 去掉gcc版本信息
CFLAGS+= -fno-builtin 				# 不需要gcc内置函数
# CFLAGS+= -nostdinc 					# 不需要标准头文件
CFLAGS+= -fno-pic 					# 不需要位置无关的代码
CFLAGS+= -fno-pie 					# 不需要位置无关的可执行程序
CFLAGS+= -nostdlib 					# 不需要标准库
CFLAGS+= -fno-stack-protector 		# 不需要栈保护
CFLAGS:=$(strip ${CFLAGS})



%.bin: boot/%.asm
	nasm -I boot/include/ $^ -f bin -o out/$@	

bootfiles = boot.bin loader.bin
boot.bin: $(bootfiles)

kernelfiles = kernel/main.c
kernel.bin: $(kernelfiles)
	nasm lib/kernel/print.asm -f elf -o out/print.o
	gcc $(CFLAGS) -I lib/kernel/ -c -o out/main.o kernel/main.c
	ld -m elf_i386 -Ttext 0xc0001500 -e main -o out/kernel.bin out/main.o out/print.o

infuq-os.img:
	bximage -q -hd=16M -mode=create -sectsize=512 -imgmode=flat infuq-os.img

all: infuq-os.img boot.bin kernel.bin
	dd if=out/boot.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc
	dd if=out/kernel.bin of=infuq-os.img bs=512 count=200 seek=9  conv=notrunc

run:
	bochs

.PHONY:clean
clean:
	@$(RM) ./out/*
	@$(RM) *.img *.ini



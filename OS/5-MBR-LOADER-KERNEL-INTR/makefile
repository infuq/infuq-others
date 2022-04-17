
%.bin: boot/%.asm
	nasm -I boot/include/ $^ -f bin -o out/$@	

bootfiles = mbr.bin loader.bin
boot.bin: $(bootfiles)

kernelfiles = kernel/main.c
kernel.bin: $(kernelfiles)
	nasm lib/kernel/print.asm -f elf -o out/print.o
	nasm kernel/kernel.asm -f elf -o out/kernel.o
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/main.o kernel/main.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/interrupt.o kernel/interrupt.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/init.o kernel/init.c

	ld -m elf_i386 -Ttext 0xc0001500 -e main -o out/kernel.bin out/main.o out/print.o out/init.o out/interrupt.o out/kernel.o

infuq-os.img:
	bximage -q -hd=16M -mode=create -sectsize=512 -imgmode=flat infuq-os.img

all: infuq-os.img boot.bin kernel.bin
	dd if=out/mbr.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc
	dd if=out/kernel.bin of=infuq-os.img bs=512 count=200 seek=9  conv=notrunc
	
run:
	bochs


.PHONY: clean
clean:
	@$(RM) ./out/*
	@$(RM) *.img *.ini



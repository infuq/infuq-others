
%.bin: boot/%.asm
	nasm -I boot/include/ $^ -f bin -o out/$@	

bootfiles = boot.bin loader.bin
boot.bin: $(bootfiles)

kernelfiles = kernel/main.c
kernel.bin: $(kernelfiles)
	nasm lib/kernel/print.asm -f elf -o out/print.o
	nasm kernel/kernel.asm -f elf -o out/kernel.o
	gcc -m32 -I ./lib/ -I ./lib/kernel -I ./lib/user -c -fno-builtin -fno-stack-protector -o out/string.o lib/string.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/bitmap.o kernel/bitmap.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/memory.o kernel/memory.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/interrupt.o kernel/interrupt.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/init.o kernel/init.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/main.o kernel/main.c

	ld -m elf_i386 -Ttext 0xc0001500 -e main -o out/kernel.bin out/main.o out/print.o out/init.o out/interrupt.o out/kernel.o out/bitmap.o out/memory.o out/string.o


all: boot.bin kernel.bin
	dd if=out/boot.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc
	dd if=out/kernel.bin of=infuq-os.img bs=512 count=200 seek=9  conv=notrunc


.PHONY:clean
clean:
	@$(RM) ./out/*



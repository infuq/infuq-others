#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>

int main(int argc, const char *argv[])
{

    int fd = open("t.txt", O_RDWR);
    int len = lseek(fd, 0, SEEK_END);

    void* ptr = mmap(NULL, len, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);
    if (ptr == MAP_FAILED)
    {
        perror("mmap error");
        exit(1);
    }

    printf("%p\n", ptr);


    // 打印内容
    printf("%s\n", (char *)ptr);

    sleep(60);


    munmap(ptr, len);
    close(fd);

	return 0;

}

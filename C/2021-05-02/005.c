#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>
#include <dirent.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{

    // ./a.out my.log           argv[1] == my.log
	int fd = open(argv[1], O_RDWR | O_CREAT, 0775);
	if (fd < 0)
	{
		perror("open file Error");
		return -1;
	}

	write(fd, "www.infuq.com", 13);

    // 从文件尾部向后扩展15个字节
	lseek(fd, 15, SEEK_END);
	write(fd, "v", 1);


	close(fd);

	return 0;

}



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


	int fd = open(argv[1], O_RDWR | O_CREAT, 0775);
	if (fd < 0)
	{
		perror("open fail");
		return -1;
	}


	dup2(fd, STDOUT_FILENO);

	printf("dup2 syscall");

	close(fd);


	return 0;

}



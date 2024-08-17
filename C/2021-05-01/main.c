#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>


int main(int argc, char *argv[])
{

	struct stat statbuf;
	stat(argv[1], &statbuf);

	if (S_ISREG(statbuf.st_mode))
	{
		puts("Regular File\n");
	}

	else if (S_ISDIR(statbuf.st_mode))
	{
		puts("Directory\n");
	}

	return 0;

}

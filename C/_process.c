#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>



int main(int argc, const char *argv[])
{


	pid_t pid;

	pid = fork();

	if (pid > 0)
	{
		printf("%d %d\n", getpid(), getppid());
	
	} else if (pid == 0)
	{
		printf("%d %d\n", getpid(), getppid());
	}
	
	

	return 0;

}

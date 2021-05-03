#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	// 创建子进程
	pid_t pid = fork();
	if (pid < 0)
	{
		perror("[fork] Error");
		return -1;
	}

	else if (pid > 0) // 父进程
	{
		sleep(100);
		printf("[parent] pid=[%d],ppid=[%d]\n", getpid(), getppid());
	}
	else if (pid == 0) // 子进程
	{
		printf("[child] pid=[%d],ppid=[%d]\n", getpid(), getppid());
	}



	return 0;
}

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
		// 为了能够使用ps -ef监控到父进程,所以先让父进程睡3秒
		sleep(3);
		printf("[parent] pid=[%d],ppid=[%d]\n", getpid(), getppid());
	}
	else if (pid == 0) // 子进程
	{
		// 先让父进程退出
		sleep(7);
		printf("[child] pid=[%d],ppid=[%d]\n", getpid(), getppid());
	}



	return 0;
}

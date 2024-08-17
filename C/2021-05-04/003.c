#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

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
		int wstatus;
		pid_t wpid = wait(&wstatus);
		if (WIFEXITED(wstatus)) // 正常退出
		{
			printf("[child]=[%d],status=[%d]\n", wpid, WEXITSTATUS(wstatus));
		}
		else if (WIFSIGNALED(wstatus)) // 被信号杀死
		{
			printf("[child]=[%d],status=[%d]\n", wpid, WTERMSIG(wstatus));
		}

	}
	else if (pid == 0) // 子进程
	{
		sleep(3);
		return 5;
	}



	return 0;
}

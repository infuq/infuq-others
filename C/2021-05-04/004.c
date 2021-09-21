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
		//pid_t wpid = waitpid(pid, &wstatus, 0); // BLOCK
		pid_t wpid = waitpid(pid, &wstatus, WNOHANG); // NONBLOCK
		if (wpid > 0)
		{
			if (WIFEXITED(wstatus)) // 正常退出
			{
				printf("1.[child]=[%d],status=[%d]\n", wpid, WEXITSTATUS(wstatus));
			}
			else if (WIFSIGNALED(wstatus)) // 被信号杀死
			{
				printf("2.[child]=[%d],status=[%d]\n", wpid, WTERMSIG(wstatus));
			}
		}
		else
		{
			printf("other...\n");
		}

		// 子进程已经变成僵尸进程
		
		
		// 父进程sleep, 可通过ps -ef查看子进程状态
		sleep(100);

	}
	else if (pid == 0) // 子进程
	{
		sleep(3);
		return 5;
	}



	return 0;
}

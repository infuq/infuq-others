#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char *argv[])
{


	int pipefd[2];
    pid_t cpid;
    char buf;


    if (pipe(pipefd) == -1) 
	{
		perror("pipe");
        exit(EXIT_FAILURE);
	}

    cpid = fork();
    if (cpid == -1) 
	{
		perror("fork");
        exit(EXIT_FAILURE);
	}

	if (cpid == 0) 
	{
		close(pipefd[1]);          

		while (read(pipefd[0], &buf, 1) > 0)
			write(STDOUT_FILENO, &buf, 1);

		write(STDOUT_FILENO, "\n", 1);
		close(pipefd[0]);
		_exit(EXIT_SUCCESS);

	} 
	else {         
		close(pipefd[0]);          
		write(pipefd[1], "xyzABC", strlen("xyzABC"));
		close(pipefd[1]);          /* Reader will see EOF */
		wait(NULL);                /* Wait for child */
		exit(EXIT_SUCCESS);
	}



	return 0;
}

#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <signal.h>


int main(int argc, const char *argv[])
{


#if 1
    // 屏蔽CTRL+C
    printf("屏蔽CTRL+C\n");
    sigset_t set;
    sigemptyset(&set);
    sigaddset(&set, SIGINT);
    sigprocmask(SIG_BLOCK, &set, NULL);

#endif

    printf("%d\n", getpid());
    sleep(60);

    return 0;

}

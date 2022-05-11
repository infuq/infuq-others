#include <sys/socket.h>
#include <sys/epoll.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 10

int main(int argc, char **argv)
{
    int efd, i;
    int pfd[2];
    pid_t pid;
    char buf[MAXLINE], ch = 'a';

    pipe(pfd);
    pid = fork();

    if (pid == 0) {// 子进程  负责向管道里写数据
        close(pfd[0]);
        while (1) {

            for (i = 0; i < MAXLINE / 2; i++)
                buf[i] = ch;
            buf[i - 1] = '\n';
            ch++;
            
            for (; i < MAXLINE; i++)
                buf[i] = ch;
            buf[i - 1] = '\n';
            ch++;

            write(pfd[1], buf, sizeof(buf));
            sleep(5);
        }
        close(pfd[1]);
    } else if (pid > 0) {   // 父进程 从管道中读取数据
        struct epoll_event ev;
        struct epoll_event event[10];
        int res, len;
        close(pfd[1]);
        efd = epoll_create(10);
        
#if 1        
        ev.events = EPOLLIN | EPOLLET;                  // ET 边沿触发
#else
        ev.events = EPOLLIN;                            // LT 水平触发(默认)
#endif
        ev.data.fd = pfd[0];
        epoll_ctl(efd, EPOLL_CTL_ADD, pfd[0], &ev);

        while (1) {
            res = epoll_wait(efd, event, 10, -1);
            //printf("res %d\n", res);
            if (event[0].data.fd = pfd[0]) {
                len = read(pfd[0], buf, MAXLINE / 2);
                write(STDOUT_FILENO, buf, len);
            }
        }
        close(pfd[0]);
        close(efd);

    }


    return 0;
}

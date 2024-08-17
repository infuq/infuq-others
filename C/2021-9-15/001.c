#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <errno.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    
    int fd = open("/dev/sda", O_RDONLY);
/*
    int flag = fcntl(fd, F_GETFL, 0);
    flag = flag & ~O_NONBLOCK;
    fcntl(fd, F_SETFL, flag);
*/
    char buf[1024];
    bzero(&buf, sizeof(buf));
    read(fd, buf, 1024);

    printf("%s\n", buf);

    return 0;
}



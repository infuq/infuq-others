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
#include <netinet/ip.h>

 
int main(int argc, char **argv)
{
    struct sockaddr_in sockaddr;

    int fd = socket(AF_INET, SOCK_STREAM, 0);
                
    bzero(&sockaddr, sizeof(sockaddr));
    sockaddr.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &sockaddr.sin_addr);
    sockaddr.sin_port=htons(6379);

    connect(fd, (struct sockaddr *)&sockaddr, sizeof(sockaddr));

    write(fd, "*3\r\n", 4);
    write(fd, "$3\r\nSET\r\n", 9);
    write(fd, "$2\r\nk3\r\n", 8);
    write(fd, "$2\r\nv3\r\n", 8);

    char buf[1024];
    memset(buf, '\0', sizeof(buf));
    read(fd, buf, sizeof(buf));
    printf("%s\n", buf);

    close(fd);

    return 0;
}

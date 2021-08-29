#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <errno.h>

#define SERV_PORT 5003
#define SERV_IP_ADDR "127.0.0.1"

int main(int argc, char* argv[])
{

    int fd = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sin;
    bzero(&sin, sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_port = htons(SERV_PORT); //网络字节序的端口号
    sin.sin_addr.s_addr = inet_addr(SERV_IP_ADDR);//
    connect(fd, (struct sockaddr*)&sin, sizeof(sin));
    


    return 0;
}

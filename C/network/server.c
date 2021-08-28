#include <sys/types.h>
#include <sys/socket.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

#define SERV_PORT 5003
#define SERV_IP_ADDR "127.0.0.1"

int main(int argc, char* argv[])
{

    int fd = socket(AF_INET, SOCK_STREAM, 0);


    struct sockaddr_in addr;
    bzero(&addr, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(SERV_PORT); //网络字节序的端口号
    addr.sin_addr.s_addr = inet_addr(SERV_IP_ADDR);//

    bind(fd, (struct sockaddr*)&addr, sizeof(addr));

    
    listen(fd, 6);


    return 0;
}

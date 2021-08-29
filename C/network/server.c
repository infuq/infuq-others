#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <errno.h>

#define SERV_PORT	5001
#define SERV_IP_ADDR	"192.168.1.170"
#define BACKLOG		5

int main( void )
{
	int			lfd = -1;
	struct socketaddr_in	sin;

	if ( (lfd = socket( AF_INET, SOCK_STREAM, 0 ) ) < 0 )
	{
		perror( "socket error" );
		exit( 1 );
	}

	bzero( &sin, sizeof(sin) );
	sin.sin_family	= AF_INET;
	sin.sin_port	= htons( SERV_PORT ); /* 网络字节序的端口号 */
#if 1
	/* sin.sin_addr.s_addr = int_addr(SERV_IP_ADDR); IP地址被指定了,无法移植到其他机器 */
	sin.sin_addr.s_addr = htonl( INADDY_ANY );
#else
	if ( inet_pton( AF_INET, SERV_IP_ADDR, (void *) &sin.sin_addr.s_addr ) != 1 )
	{
		perror( "inet_pton error" );
		exit( 1 );
	}
#endif
	if ( bind( lfd, (struct socketaddr *) &sin, sizeof(sin) ) < 0 )
	{
		perror( "bind error" );
		exit( 1 );
	}

	if ( listen( lfd, BACKLOG ) < 0 )
	{
		perror( "listen error" );
		exit( 1 );
	}

	int fd = -1;
	/* 阻塞等待客户端连接 */
#if 0
	fd = accept( lfd, NULL, NULL );
	if ( fd < 0 )
	{
		perror( "accept error" );
		exit( 1 );
	}
#else
	struct sockaddr_in	cin;
	socklen_t		addrlen = sizeof(cin);
	if ( (fd = accept( lfd, (struct sockaddr *) &cin, &addrlen ) ) < 0 )
	{
		perror( "accept error" );
		exit( 1 );
	}
	/* 获取刚建立连接的客户端的IP地址和端口号 */
	char ipv4_addr[16];
	if ( !inet_ntop( AF_INET, (void *) &cin.sin_addr.s_addr, ipv4_addr, sizeof(cin) ) )
	{
		perror( "inet_ntop error" );
		exit( 1 );
	}
	printf( "客户端(%s:%d)连接到服务器!\n", ipv4_addr, ntohs( cin.sin_port ) );
#endif


	int	ret = -1;
	char	buf[BUFSIZ];

	while ( 1 )
	{
		bzero( buf, BUFSIZ );
		do
		{
			ret = read( fd, buf, BUFSIZ - 1 );
		}
		while ( ret < 0 && EINTR == errno );
		if ( ret < 0 )
		{
			perror( "read error" );
			exit( 1 );
		}
		if ( 0 == ret ) /* 对方已经关闭 */
		{
			break;
		}
		printf( "接收到的数据 %s\n", buf );
	}

	close( fd );
	close( lfd );

	return(0);
}
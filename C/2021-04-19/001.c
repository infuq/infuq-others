#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>



int main(int argc, const char *argv[])
{


	// 虽然没有\0, 但是依然可以打印正确, 那是因为字符后面没有多余的字符.
	//char arr[] = {'a', 'b', 'c', '1'};
	//printf("%s\n", arr);


	// 没有\0, 内容打印就会错误
	char arr[] = {'a', 'b', 'c', '1'};
	char tmp[] = "向缓冲里面追\0加一些数据";
	printf("%s\n", arr);


	return 0;

}

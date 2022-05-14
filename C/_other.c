#include<stdio.h>
#include<string.h>

void _memset()
{
    char content[] = "this is a test";
    printf("%s\n", content);

    memset(content, '-', 4);
    printf("%s\n", content);

}


int count = 0;
int _fib(int n)
{

    count += 1;
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;

    return _fib(n - 1) + _fib(n - 2);
}

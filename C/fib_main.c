#include<stdio.h>

'''
斐波那契数列
'''


int fib(int n)
{
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    
    return fib(n - 1) + fib(n - 2);
}


int main()
{

    int f = fib(40);
    printf("%d\n", f);

    return 0;
}


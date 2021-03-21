#include<stdio.h>

/*
枚举的大小
*/

enum Color
{
    RED,
    GREEN,
    BLUE
};

int main()
{
    enum Color color = RED;

    printf("%d\n", sizeof(color));

    return 0;
}
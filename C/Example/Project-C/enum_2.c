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

void enum_2()
{
    enum Color color = RED;

    printf("%d\n", sizeof(color));


}
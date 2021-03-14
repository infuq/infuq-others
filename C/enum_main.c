#include<stdio.h>

enum Color
{
    // 常量
    RED,
    GREEN,
    BLUE
};

enum Sex
{
    // 常量
    MALE = 1,
    FEMALE = 2
};

int main()
{

    enum Color color = RED;
    printf("%d %d %d\n", RED, GREEN, BLUE);

    printf("%d %d\n", MALE, FEMALE);

    return 0;
}


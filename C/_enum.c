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
            MALE = 3,
    FEMALE = 2
};

void _enum()
{

    enum Color color = RED;
    // 这种是有问题的, 虽然值RED等于0, 但是左右类型不一致
    enum Color color2 = 0;

    printf("%d %d %d\n", RED, GREEN, BLUE);
    printf("%d %d\n", MALE, FEMALE);

}


void _enum_2()
{

    enum Color color = RED;
    printf("%lu\n", sizeof(color));

}

#include<stdio.h>


// 判断大小端的第一种方式
void invoke_1()
{
    int a = 0x02000001;

    char *ptr = (char *) &a;
    printf("%d\n", *ptr);// =1   小端存储

    printf("%d\n", *(ptr+3));// =2
}


union Un
{
    char c;
    int i;
};
// 判断大小端的第二种方式
void invoke_2()
{
    union Un data;
    data.i = 0x000000001;

    printf("%d\n", data.c);

}


int main()
{


    invoke_2();
    


    return 0;
}
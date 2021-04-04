#include<stdio.h>


struct
{
    int a;
    char c;
} stu;

struct
{
    int a;
    char c;
}  *ptr, stu2;


int main()
{

    // ptr = &stu;  Error
    ptr = &stu2;

    return 0;

}



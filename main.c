#include<stdio.h>


typedef struct stu
{
    struct stu *next;
    // Stu *next;
    int age;
    
    char c;
    char arr[20];
} Stu;

int main()
{
    
    // stu1 -> stu2 -> stu3

    Stu stu3, stu2, stu1;
    stu3.c = '3';
    stu2.c = '2';
    stu1.c = '1';

    stu2.next = &stu3;
    stu1.next = &stu2;

    // printf("%c\n", stu1.next->next->c);

    printf("%d\n", sizeof(Stu));
    printf("%d\n", sizeof(stu1));

    return 0;
}
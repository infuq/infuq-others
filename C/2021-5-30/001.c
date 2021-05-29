#include <stdio.h>


int main()
{

    int arr[] = { 1,2,3,4,5 };

    int (*ptr)[5] = arr;// 虽然也可以这么写,但严格讲,不正确. 正确写法: int* ptr = arr;
    printf("%p\n", ptr);
    printf("%p\n\n", ptr + 1);

    int (*ptr2)[5] = &arr;// 正确
    printf("%p\n", ptr2);
    printf("%p\n", ptr2 + 1);

    return 0;
}
/*
输出结果

0x7ffff4a8d720
0x7ffff4a8d734

0x7ffff4a8d720
0x7ffff4a8d734

*/

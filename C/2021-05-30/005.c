#include <stdio.h>

int main()
{

    // arr1和arr2的内容存储在内存的动态存储区(堆)
    char arr1[] = "abcdef";
    char arr2[] = "abcdef";

    printf("&arr1=%p\n", &arr1);
    printf("&arr2=%p\n", &arr2);

    char *ptr1 = arr1;
    *ptr1 = 'K';
    printf("arr1=%s\n\n", arr1);



    // p1和p2指向的内容存储在内存的静态存储区
    // p1和p2指向字符'a'的地址
    char *p1 = "abcdef";
    char *p2 = "abcdef";
   
    // 由于"abcdef"是常量字符串, 不可以被修改, 因此这里的赋值会报错
    *p1 = 'Q';

    printf("p1=%p\n", p1);
    printf("p2=%p\n", p2);

    return 0;
}
/*
输出结果

&arr1=0x7fffcff7470a
&arr2=0x7fffcff74711

p1=0x7fa069c00804
p2=0x7fa069c00804

*/

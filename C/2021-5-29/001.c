#include <stdio.h>

int main()
{
    
    int arr[3][4] = { {1,2,3,4},{5,6,7,8},{9,10,11,12} };
    
    int* ptr = arr;// 虽然也可以这么写,但严格讲,不正确
    printf("%p\n", ptr);
    printf("%p\n\n", ptr+1);

    // 数组名表示数组首元素的地址.那么arr表示数组首元素(arr[0]={1,2,3,4})的地址
    int(*ptr2)[4] = arr;// 正确
    printf("%p\n", ptr2);
    printf("%p\n\n", ptr2 + 1);

    int (*ptr3)[3][4] = arr;// 虽然也可以这么写,但严格讲,不正确
    printf("%p\n", ptr3);
    printf("%p\n\n", ptr3 + 1);

    int(*ptr4)[3][4] = &arr;// 正确
    printf("%p\n", ptr4);
    printf("%p\n\n", ptr4 + 1);

    return 0;
}

/*
输出结果

0x7ffffa60cb60
0x7ffffa60cb64

0x7ffffa60cb60
0x7ffffa60cb70

0x7ffffa60cb60
0x7ffffa60cb90

0x7ffffa60cb60
0x7ffffa60cb90

*/










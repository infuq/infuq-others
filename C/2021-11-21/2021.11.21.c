#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *thread1(void *arg)
{
    pthread_t newthid;

    newthid = pthread_self();
    printf("child thread1, thread ID = %ld\n", newthid);


    int k = 20;
    printf("线程1中变量k地址\t = %p\n", &k);

    int size = 17 * 1024 * 1024;// 17M
    void *ptr = malloc(size);
    printf("线程1中申请堆空间地址\t = %p\n", ptr);


    int i = 10;
    printf("线程1中变量i地址\t = %p\n", &i);


    sleep(3600);
    return NULL;
}

void *thread2(void *arg)
{
    pthread_t newthid;

    newthid = pthread_self();
    printf("child thread2, thread ID = %ld\n", newthid);


    int k = 20;
    printf("线程2中变量k地址\t = %p\n", &k);

    int size = 10 * 1024 * 1024;// 10M
    void *ptr = malloc(size);
    printf("线程2中申请堆空间地址\t = %p\n", ptr);


    int i = 10;
    printf("线程2中变量i地址\t = %p\n", &i);


    sleep(3600);
    return NULL;
}

int main(void)
{
    pthread_t tid1;
    pthread_t tid2;

    printf("main thread ,thread ID = %ld\n", pthread_self());


#if 1
    if (pthread_create(&tid1, NULL, (void *)thread1, NULL) != 0) {
        printf("thread creation failed\n");
        exit(1);
    }
    if (pthread_create(&tid2, NULL, (void *)thread2, NULL) != 0) {
        printf("thread creation failed\n");
        exit(1);
    }
#endif

    sleep(3);


    int k = 20;
    printf("主线程中变量k地址\t = %p\n", &k);

    int size = 14 * 1024 * 1024;//14M
    void *ptr = malloc(size);
    printf("主线程中申请堆空间地址\t = %p\n", ptr);

    int i = 10;
    printf("主线程中变量i地址\t = %p\n", &i);

    sleep(3600);
    return 0;
}


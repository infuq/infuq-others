#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
 
void *thread(void *arg)
{
    pthread_t newthid;
         
    newthid = pthread_self();
    printf("this is a new thread, thread ID = %ld\n", newthid);
    

    sleep(30);
    return NULL;
}
 
int main(void)
{
    pthread_t thid;
         
    printf("main thread ,ID is %ld\n", pthread_self());
    
    if (pthread_create(&thid, NULL, (void *)thread, NULL) != 0) {
        printf("thread creation failed\n");
        exit(1);
    }
   
    // 主线程调用return会导致进程退出.

    return 0;
}

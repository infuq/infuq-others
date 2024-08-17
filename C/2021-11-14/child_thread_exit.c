#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
 
void *thread(void *arg)
{
    pthread_t newthid;
         
    newthid = pthread_self();
    printf("this is a new thread, thread ID = %ld\n", newthid);
    
//  子线程调用return 或 pthread_exit并不会导致进程退出, 且子线程正常退出.
//    pthread_exit(NULL);

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
   

    sleep(30);

    return 0;
}

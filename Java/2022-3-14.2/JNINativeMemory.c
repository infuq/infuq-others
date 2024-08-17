#include "jni.h"
#include "JNINativeMemory.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>

JNIEXPORT void JNICALL Java_JNINativeMemory_allocateMemory(JNIEnv *env, jobject j) {
    // 32MB = 33554432
    
    void *ptr = mmap(NULL, 33554432, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    printf("C'mmap 申请 %p\n", ptr);

    //
    //void *ptr = malloc(32 * 1024 * 1024);
    //printf("C'malloc 申请 %p\n", ptr);
}

#include "jni.h"
#include "JNINativeMemory.h"
#include <stdlib.h>
#include <stdio.h>

JNIEXPORT void JNICALL Java_JNINativeMemory_allocateMemory(JNIEnv *env, jobject j) {
    void *ptr = malloc(1000);
    printf("> %p\n", ptr);
}

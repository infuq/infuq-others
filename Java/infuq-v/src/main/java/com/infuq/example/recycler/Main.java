package com.infuq.example.recycler;

import io.netty.util.Recycler;
import io.netty.util.concurrent.FastThreadLocalThread;

import java.util.concurrent.locks.LockSupport;

public class Main {


    private static final Recycler<Book> BOOK = new Recycler<Book>() {
        @Override
        protected Book newObject(Handle<Book> handle) {
            return new Book(handle);
        }
    };


    private static Book book1;
    private static Book book2;
    private static Book book3;

    public static void main(String[] args) throws Exception {


        new FastThreadLocalThread(() -> {
            // book1,book2,book3都是从线程Thread-1中创建产生
            book1 = BOOK.get();
            book1.setName("Java");

            book2 = BOOK.get();
            book2.setName("C");

            book3 = BOOK.get();
            book3.setName("C++");
            // book1在线程Thread-1中回收
            book1.recycle();


            new FastThreadLocalThread(() -> {
                // book2在线程Thread-2中回收
                book2.recycle();
                LockSupport.park();// 让线程不退出,便于观察
            }, "Thread-2").start();


            new FastThreadLocalThread(() -> {
                // book3在线程Thread-3中回收
                book3.recycle();
                LockSupport.park();// 让线程不退出,便于观察
            }, "Thread-3").start();


            LockSupport.park();// 让线程不退出,便于观察
        }, "Thread-1").start();


        // 让线程不退出,便于观察
        LockSupport.park();



    }



}

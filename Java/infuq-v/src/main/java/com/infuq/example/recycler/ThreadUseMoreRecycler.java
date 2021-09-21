package com.infuq.example.recycler;

import io.netty.util.Recycler;
import io.netty.util.concurrent.FastThreadLocalThread;
import java.util.concurrent.locks.LockSupport;

public class ThreadUseMoreRecycler {


    private static final Recycler<Book> BOOK_CN = new Recycler<Book>() {
        @Override
        protected Book newObject(Handle<Book> handle) {
            return new Book(handle);
        }
    };


    private static final Recycler<Book> BOOK_EN = new Recycler<Book>() {
        @Override
        protected Book newObject(Handle<Book> handle) {
            return new Book(handle);
        }
    };


    public static void main(String[] args) throws Exception {


        new FastThreadLocalThread(() -> {

            // 在同一个线程中使用多个Recycler实例,则会创建多个Stack
            Book book1 = BOOK_CN.get();
            Book book2 = BOOK_EN.get();


            LockSupport.park();
        }, "Thread-1").start();

        System.out.println("start thread-1...");

        LockSupport.park();


    }
}

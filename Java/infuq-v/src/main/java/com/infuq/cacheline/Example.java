package com.infuq.cacheline;

import org.junit.Test;

import java.util.concurrent.CountDownLatch;

public class Example {

    public static void main(String[] args) throws Exception {

//        t1();
        t2();

    }


    static void t1() throws Exception {

        long count = 100000000L;
        CountDownLatch latch = new CountDownLatch(2);
        long start = System.nanoTime();

        V1[] arr = new V1[2];
        arr[0] = new V1();
        arr[1] = new V1();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (long i = 0; i < count; i++) {
                    arr[0].year = i;
                }
                latch.countDown();
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (long i = 0; i < count; i++) {
                    arr[1].year = i;
                }
                latch.countDown();
            }
        }).start();

        latch.await();

        System.out.println(System.nanoTime() - start);


    }


    static void t2() throws Exception {

        long count = 100000000L;
        CountDownLatch latch = new CountDownLatch(2);
        long start = System.nanoTime();

        V2[] arr = new V2[2];
        arr[0] = new V2();
        arr[1] = new V2();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (long i = 0; i < count; i++) {
                    arr[0].year = i;
                }
                latch.countDown();
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                for (long i = 0; i < count; i++) {
                    arr[1].year = i;
                }
                latch.countDown();
            }
        }).start();

        latch.await();

        System.out.println(System.nanoTime() - start);


    }



}

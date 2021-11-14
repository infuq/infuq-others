package com.infuq.thread;

public class Example {


    public static void main(String[] args) {


        new Thread(() -> {

            try {
                Thread.sleep(30000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println("ChildThread...");

        }).start();


        try {
            Thread.sleep(20000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("MainThread...");


    }

}

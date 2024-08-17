package com.infuq.classloader;

public class Parent {

    private static final int year = 2022;
    private static String address = "Chengdu";

    static {
        System.out.println("Parent静态代码块");
    }

    private String color = "orange";

    {
        System.out.println("Parent实例代码块");
    }

    Parent() {
        System.out.println("Parent构造器");
    }


}

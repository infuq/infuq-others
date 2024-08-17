package com.infuq.classloader;

public class Child extends Parent {


    private static final int i = 2000;
    private static String city = "Hangzhou";

    static {
        System.out.println("Child静态代码块");
    }

    private String computer = "惠普";

    {
        System.out.println("Child实例代码块");
    }

    Child() {
        System.out.println("Child构造器");
    }



}

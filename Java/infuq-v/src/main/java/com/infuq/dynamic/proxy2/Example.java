package com.infuq.dynamic.proxy2;

import java.lang.reflect.Proxy;

public class Example {

    public static void main(String[] args) {

        Engineer javaEngineer = new JavaEngineer();
        MyProxyHandler handler = new MyProxyHandler(javaEngineer);
        Engineer proxy = (Engineer) Proxy.newProxyInstance(Engineer.class.getClassLoader(),
                new Class[]{Engineer.class}, handler);

        proxy.query();

    }

}

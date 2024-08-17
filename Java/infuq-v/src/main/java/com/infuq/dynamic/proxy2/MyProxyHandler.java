package com.infuq.dynamic.proxy2;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class MyProxyHandler implements InvocationHandler {

    private Object target;

    public MyProxyHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("before ...");
        Object result = method.invoke(target, args);
        System.out.println("after ...");
        return result;
    }
}

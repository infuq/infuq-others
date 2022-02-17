package com.infuq.dynamic.proxy;

import org.springframework.cglib.proxy.MethodInterceptor;
import org.springframework.cglib.proxy.MethodProxy;
import java.lang.reflect.Method;

public class MyServiceInterceptor implements MethodInterceptor {

    @Override
    public Object intercept(Object obj, Method method, Object[] objects, MethodProxy methodProxy) throws Throwable {
        System.out.println("before ...");
        Object result = methodProxy.invokeSuper(obj, objects);
        System.out.println("after ...");
        return result;
    }

}

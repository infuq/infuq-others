package com.infuq.dynamic.proxy;

import org.springframework.cglib.core.DebuggingClassWriter;
import org.springframework.cglib.proxy.Enhancer;

public class Example {

    public static void main(String[] args) {

        //设置代理类生成目录
        System.setProperty(DebuggingClassWriter.DEBUG_LOCATION_PROPERTY, "D:\\tmp");
        Enhancer enhancer = new Enhancer();
        //设置超类. 因为CGLIB基于父类生成代理子类
        enhancer.setSuperclass(RealService.class);
        //设置回调,也就是我们的拦截处理
        enhancer.setCallback(new MyServiceInterceptor());

        //创建代理类
        RealService realService = (RealService) enhancer.create();
        //调用代理类的方法
        realService.realMethod();
    }

}

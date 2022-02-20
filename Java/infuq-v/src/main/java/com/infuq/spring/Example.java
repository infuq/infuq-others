package com.infuq.spring;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Example {


    public static void main(String[] args) {

        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(MyConfig.class);


        Object v1 = context.getBean("&bookFactoryBean");

        System.out.println(v1);

        Object v2 = context.getBean("bookFactoryBean");

        System.out.println(v2);
    }










}

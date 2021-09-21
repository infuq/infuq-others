package com.infuq.spring;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Example {


    public static void main(String[] args) {

        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(MyConfig.class);


        Computer bean = context.getBean(Computer.class);

        System.out.println(bean);


    }










}

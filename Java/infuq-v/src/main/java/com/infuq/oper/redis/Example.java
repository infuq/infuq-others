package com.infuq.oper.redis;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Example {

    public static void main(String[] args) {

        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(MyConfig.class);
        RedisUtil redisUtil = context.getBean(RedisUtil.class);

        redisUtil.hashPut("k1", "hk1", "hv1");
        redisUtil.hashPut("k1", "hk2", "hv2");
        Object o = redisUtil.hashGet("k1", "hk1");
        System.out.println(o);

//        Object o = redisUtil.get("123");
//        System.out.println(o);


    }

}

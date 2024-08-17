package com.infuq.rate.limiter;

public class Counter {

    private static long start = System.currentTimeMillis();

    // 限制在1s内只允许100请求
    private static final long MAX_COUNT = 100;
    private static final long interval = 1000;// 1s

    // 请求数
    private static long currentReqCount = 0;

    public static boolean grant() {
        long now = System.currentTimeMillis();
        if (now < start + interval) {
            if (currentReqCount < MAX_COUNT) {
                ++currentReqCount;
                return true;
            } else {
                return false;
            }
        } else {
            start = System.currentTimeMillis();
            currentReqCount = 0;
            return false;
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 500; i++) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    if (grant()) {
                        System.out.println("执行业务逻辑");
                    } else {
                        System.out.println("限流");
                    }
                }
            }).start();
        }
    }
}

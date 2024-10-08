package com.infuq.distributed.lock;

import org.redisson.Redisson;
import org.redisson.RedissonRedLock;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;
import org.redisson.config.Config;
import java.util.concurrent.TimeUnit;


public class RedLockExample {

    public static void main(String[] args) throws InterruptedException {


        Config config1 = new Config();
        config1.useSingleServer().setAddress("redis://192.168.0.1:6379").setPassword("password").setDatabase(0);
        RedissonClient redissonClient1 = Redisson.create(config1);

        Config config2 = new Config();
        config2.useSingleServer().setAddress("redis://192.168.0.2:6379").setPassword("password").setDatabase(0);
        RedissonClient redissonClient2 = Redisson.create(config2);

        Config config3 = new Config();
        config3.useSingleServer().setAddress("redis://192.168.0.3:6379").setPassword("password").setDatabase(0);
        RedissonClient redissonClient3 = Redisson.create(config3);


        String resourceName = "REDLOCK";
        RLock lock1 = redissonClient1.getLock(resourceName);
        RLock lock2 = redissonClient2.getLock(resourceName);
        RLock lock3 = redissonClient3.getLock(resourceName);


        RedissonRedLock redLock = new RedissonRedLock(lock1, lock2, lock3);

        boolean isLock;

        isLock = redLock.tryLock(500, 30000, TimeUnit.MILLISECONDS);
        if (isLock) {

            try {
                // 获取到锁, 执行业务流程

            } catch (Exception e) {

            } finally {
                // 无论如何, 最后都要解锁
                redLock.unlock();
            }
        }



    }



}

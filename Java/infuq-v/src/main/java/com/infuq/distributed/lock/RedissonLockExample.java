package com.infuq.distributed.lock;
import org.redisson.Redisson;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;
import org.redisson.config.Config;
import java.util.concurrent.TimeUnit;



public class RedissonLockExample {


    public static void main(String[] args) {


        Config config = new Config();

        // 单机模式
        config.useSingleServer().setAddress("redis://192.168.0.1:6379");

        // 哨兵模式
        config.useSentinelServers().addSentinelAddress("redis://192.168.0.1:26379", "redis://192.168.0.2:26379", "redis://192.168.0.3:26379").setMasterName("masterName");

        // 集群模式
        config.useClusterServers().addNodeAddress(
                        "redis://192.168.0.1:6379", "redis://192.168.0.2:6379", "redis://192.168.0.3:6379",
                        "redis://192.168.0.4:6379", "redis://192.168.0.5:6379", "redis://192.168.0.6:6379")
                .setScanInterval(5000);

        // 主从模式
        config.useMasterSlaveServers().setMasterAddress("redis://192.168.0.1:6379").addSlaveAddress("redis://192.168.0.2:6379", "redis://192.168.0.3:6379");

        RedissonClient redissonClient = Redisson.create(config);
        RLock redissonLock = redissonClient.getLock("myLock");// 获取锁实例

        try {

            long waitTime = 3000;
            long leaseTime = 5000;
            // waitTime 尝试获取锁的最大等待时间,超过这个值还未获取到锁,则获取锁失败
            // leaseTime 锁的过期时间,超过这个时间锁会自动失效(值应设置为大于业务处理的时间,确保在锁的有效期内业务能处理完成)
            boolean isLock = redissonLock.tryLock(waitTime, leaseTime, TimeUnit.MILLISECONDS);

            if (isLock) {
                // 获取到锁, 执行业务流程
            }

        } catch (Exception e) {

        } finally {
            // 无论如何, 最后都要解锁
            redissonLock.unlock();
        }



    }


}

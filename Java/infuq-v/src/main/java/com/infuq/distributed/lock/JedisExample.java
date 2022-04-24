package com.infuq.distributed.lock;

import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import redis.clients.jedis.*;

import java.util.HashSet;
import java.util.Set;

public class JedisExample {

    public static void main(String[] args) {


        // 单机
        Jedis jedis = new Jedis("192.168.0.1", 6379, 3000, 5000);
        jedis.auth("password");
        jedis.select(0);// 选择库

        jedis.close();


        // 连接池
        JedisPoolConfig jedisPoolConfig = new JedisPoolConfig();
        jedisPoolConfig.setMaxTotal(8);
        jedisPoolConfig.setMaxIdle(8);
        jedisPoolConfig.setMinIdle(3);
        jedisPoolConfig.setMaxWaitMillis(200);
        JedisPool jedisPool = new JedisPool(jedisPoolConfig, "192.168.0.1", 6379, 1000, "password");

        jedisPool.getResource();




        // 集群
        Set<HostAndPort> nodes = new HashSet<>();
        nodes.add(new HostAndPort("192.168.0.1", 6379));
        nodes.add(new HostAndPort("192.168.0.2", 6379));
        nodes.add(new HostAndPort("192.168.0.3", 6379));
        GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig();
        poolConfig.setMaxIdle(10);
        JedisCluster jedisCluster = new JedisCluster(nodes, 3000, 3, poolConfig);


    }


}

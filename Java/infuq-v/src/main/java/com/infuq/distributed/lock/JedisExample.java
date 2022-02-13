package com.infuq.distributed.lock;

import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisCluster;

import java.util.HashSet;
import java.util.Set;

public class JedisExample {

    public static void main(String[] args) {


        // 单机
        Jedis jedis = new Jedis("192.168.0.1", 6379, 3000, 5000);


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

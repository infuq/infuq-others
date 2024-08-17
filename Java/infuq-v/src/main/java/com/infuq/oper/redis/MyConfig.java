package com.infuq.oper.redis;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.data.redis.connection.*;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.*;

import redis.clients.jedis.JedisPoolConfig;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;


@Configuration
@ComponentScan(basePackages = {"com.infuq.oper.redis"})
@PropertySource("classpath:redis.properties")
public class MyConfig {

    @Value("${spring.redis.host}")
    private String host;
    @Value("${spring.redis.port}")
    private Integer port;
    @Value("${spring.redis.database}")
    private int dbIndex;
    @Value("${spring.redis.password}")
    private String password;
    @Value("${spring.redis.ssl}")
    private boolean ssl;
    @Value("${spring.redis.timeout}")
    private long timeout;
    @Value("${spring.redis.jedis.pool.maxIdle}")
    private int poolMaxIdle;
    @Value("${spring.redis.jedis.pool.minIdle}")
    private int poolMinIdle;
    @Value("${spring.redis.jedis.pool.maxWait}")
    private long poolMaxWait;
    @Value("${spring.redis.sentinel.master}")
    private String sentinelMaster;
    @Value("${spring.redis.sentinel.nodes}")
    private String sentinelNodes;
    @Value("${spring.redis.cluster.nodes}")
    private String clusterNodes;
    @Value("${redis_max_redirections}")
    private int clusterMaxRedirect;
    @Value("${app.name}")
    private String appName;


    @Bean
    public JedisPoolConfig jedisPoolConfig() {
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxIdle(this.poolMaxIdle);
        config.setMinIdle(this.poolMinIdle);
        config.setMaxWaitMillis(this.poolMaxWait);

        return config;
    }


    @Bean
    public JedisConnectionFactory redisConnectionFactory(JedisPoolConfig jedisPoolConfig) {

        JedisConnectionFactory factory = this.processFactory();

        factory.setPoolConfig(jedisPoolConfig);
        return factory;
    }

    public JedisConnectionFactory processFactory() {
        if (StringUtils.isNotEmpty(this.host) && StringUtils.isEmpty(this.clusterNodes) && StringUtils.isEmpty(this.sentinelNodes)) {
            RedisStandaloneConfiguration standalone = new RedisStandaloneConfiguration();
            standalone.setPort(this.port);
            standalone.setHostName(this.host);
            if (!StringUtils.isEmpty(this.password)) {
                standalone.setPassword(this.password);
            }

            standalone.setDatabase(this.dbIndex);
            return new JedisConnectionFactory(standalone);
        } else if (StringUtils.isEmpty(this.host) && !StringUtils.isEmpty(this.clusterNodes) && StringUtils.isEmpty(this.sentinelNodes)) {
            RedisClusterConfiguration cluster = new RedisClusterConfiguration();
            String[] nodes = this.clusterNodes.split(",");
            List<RedisNode> nodeList = Arrays.stream(nodes).filter(Objects::nonNull).map((node) -> {
                return new RedisNode(node.split(":")[0], Integer.parseInt(node.split(":")[1]));
            }).collect(Collectors.toList());
            cluster.setClusterNodes(nodeList);
            if (!StringUtils.isEmpty(this.password)) {
                cluster.setPassword(this.password);
            }

            cluster.setMaxRedirects(this.clusterMaxRedirect);
            return new JedisConnectionFactory(cluster);
        } else if (StringUtils.isEmpty(this.host) && StringUtils.isEmpty(this.clusterNodes) && !StringUtils.isEmpty(this.sentinelNodes)) {
            RedisSentinelConfiguration sentinel = new RedisSentinelConfiguration();
            sentinel.setDatabase(this.dbIndex);
            if (!StringUtils.isEmpty(this.sentinelMaster)) {
                sentinel.setMaster(this.sentinelMaster);
            }

            if (!StringUtils.isEmpty(this.password)) {
                sentinel.setPassword(this.password);
            }

            List<RedisNode> nodes = Arrays.stream(this.sentinelNodes.split(",")).filter(Objects::nonNull).map((node) -> {
                return new RedisNode(node.split(":")[0], Integer.parseInt(node.split(":")[1]));
            }).collect(Collectors.toList());
            sentinel.setSentinels(nodes);
            return new JedisConnectionFactory(sentinel);
        }

        return null;
    }



    @Bean
    public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory redisConnectionFactory) {
        StringRedisTemplate t = new StringRedisTemplate(redisConnectionFactory);
        t.setKeySerializer(new RedisSerializer<String>() {
            @Override
            public byte[] serialize(String str) throws SerializationException {
                return str.getBytes(StandardCharsets.UTF_8);
            }

            @Override
            public String deserialize(byte[] bytes) throws SerializationException {
                return bytes == null ? null : new String(bytes, StandardCharsets.UTF_8);
            }
        });
        return t;
    }

    @Bean
    public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {

        RedisTemplate<Object, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(redisConnectionFactory);

        Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer<>(Object.class);

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        objectMapper.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
        objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);

        objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        jackson2JsonRedisSerializer.setObjectMapper(objectMapper);


        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);
        redisTemplate.setHashValueSerializer(jackson2JsonRedisSerializer);
        redisTemplate.afterPropertiesSet();

        return redisTemplate;
    }



}

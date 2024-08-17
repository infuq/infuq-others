package com.infuq.oper.redis;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.Cursor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ScanOptions;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;
import java.io.IOException;
import java.util.Map;


@Component
public class RedisUtil {

    @Autowired
    private StringRedisTemplate stringRedisTemplate;
    @Autowired
    private RedisTemplate<Object, Object> redisTemplate;

    public Object get(String key) {
        return key == null ? null : redisTemplate.opsForValue().get(key);
    }

    public void hashPut(String key, Object hashKey, Object value) {
        stringRedisTemplate.opsForHash().put(key, hashKey, value);
    }

    public Object hashGet(String key, Object hashKey) {

        return stringRedisTemplate.opsForHash().get(key, hashKey);
    }

    public Long hashDelete(String key, Object hashKey) {
        return stringRedisTemplate.opsForHash().delete(key, hashKey);
    }

    public Map.Entry<Object, Object> scan(String key, int limit) {

        Cursor<Map.Entry<Object, Object>> cursor = stringRedisTemplate.opsForHash().
                scan(key, ScanOptions.scanOptions().count(limit).build());

        Map.Entry<Object, Object> next = cursor.next();

        try {
            if (!cursor.isClosed()){
                cursor.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }


        return next;


    }

}

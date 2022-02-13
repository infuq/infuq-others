"if (redis.call('exists', KEYS[1]) == 0) then " + // 判断key是否存在
    "redis.call('hset', KEYS[1], ARGV[2], 1); " + // 加锁key
    "redis.call('expire', kEYS[1], ARGV[1]); " +  // 过期时间
    "return nil; " +
"end; " +
"if (redis.call('hexists', KEYS[1], ARGV[2]) == 1) then " +  // 判断锁key的Hash数据结构中是否包含客户端(自身)的ID
    "redis.call('hincrby', KEYS[1], ARGV[2], 1); " + // 可重入
    "redis.call('pexpire', KEYS[1], ARGV[1]); " +
    "return nil; " +
"end; " +
"return redis.call('pttl', KEYS[1]);" // 返回锁key的剩余生存时间


KYES[1]表示key = myLock
ARGV[1]表示过期时间,默认30秒
ARGV[2]表示加锁的客户端ID,类似8743c9c0-0795-4907-87fd-6c719a6b4586:1
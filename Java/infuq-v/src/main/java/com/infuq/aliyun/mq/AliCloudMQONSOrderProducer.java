package com.infuq.aliyun.mq;

import com.aliyun.openservices.ons.api.Message;
import com.aliyun.openservices.ons.api.ONSFactory;
import com.aliyun.openservices.ons.api.PropertyKeyConst;
import com.aliyun.openservices.ons.api.SendResult;
import com.aliyun.openservices.ons.api.order.OrderProducer;
import java.util.Properties;


/**
 *
 * TCP 协议客户端接入点
 *
 */
public class AliCloudMQONSOrderProducer {

    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put(PropertyKeyConst.GROUP_ID, "");
        properties.put(PropertyKeyConst.AccessKey, "");
        properties.put(PropertyKeyConst.SecretKey, "");
        properties.put(PropertyKeyConst.NAMESRV_ADDR, "");
        OrderProducer producer = ONSFactory.createOrderProducer(properties);
        producer.start();

        for (int i = 0; i < 1000; i++) {
            String orderId = "biz_" + i % 10;
            Message msg = new Message(
                    "",
                    "M_PAY_SUCCESS",
                    "send order global msg".getBytes()
            );
            // 重要属性
            msg.setKey(orderId);
            // 重要属性
            String shardingKey = String.valueOf(orderId);

            try {
                SendResult sendResult = producer.send(msg, shardingKey);
            } catch (Exception ignored) { }
        }

        producer.shutdown();

    }

}
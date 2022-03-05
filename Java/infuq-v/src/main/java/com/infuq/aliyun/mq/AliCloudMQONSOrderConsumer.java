package com.infuq.aliyun.mq;

import com.aliyun.openservices.ons.api.Message;
import com.aliyun.openservices.ons.api.ONSFactory;
import com.aliyun.openservices.ons.api.PropertyKeyConst;
import com.aliyun.openservices.ons.api.order.ConsumeOrderContext;
import com.aliyun.openservices.ons.api.order.MessageOrderListener;
import com.aliyun.openservices.ons.api.order.OrderAction;
import com.aliyun.openservices.ons.api.order.OrderConsumer;
import java.util.Properties;


/**
 *
 * TCP 协议客户端接入点
 *
 */
public class AliCloudMQONSOrderConsumer {

    public static void main(String[] args) {

        // 公网
        final String host = "";
        final String instance_id = "";
        final String access_id = "";
        final String access_key = "";

        final String topic = "";
        final String group_id = "";

        Properties properties = new Properties();
        properties.setProperty(PropertyKeyConst.GROUP_ID, group_id);
        properties.put(PropertyKeyConst.AccessKey, access_id);
        properties.put(PropertyKeyConst.SecretKey, access_key);
        properties.put(PropertyKeyConst.NAMESRV_ADDR, host);
        properties.put(PropertyKeyConst.ConsumeThreadNums, "16");
        properties.put(PropertyKeyConst.SuspendTimeMillis, "100");
        properties.put(PropertyKeyConst.MaxReconsumeTimes, "1");
        properties.put(PropertyKeyConst.INSTANCE_ID, instance_id);
        // 很重要属性
        properties.put(PropertyKeyConst.ALLOCATE_MESSAGE_QUEUE_STRATEGY, PropertyKeyConst.ALLOCATE_MESSAGE_QUEUE_STRATEGY);

        OrderConsumer consumer = ONSFactory.createOrderedConsumer(properties);

        consumer.subscribe(topic, "*", new MessageOrderListener() {

            public OrderAction consume(Message message, ConsumeOrderContext context) {

                System.out.println(Thread.currentThread().getName() + "\t" + message.getMsgID() + "第" + message.getReconsumeTimes() + "次数被消费");

                return OrderAction.Success;
            }
        });


        consumer.start();

        System.out.println("启动成功...");


        try {
            Thread.sleep(1000 * 60 * 60);
        } catch (Exception ignored) {

        }


    }
}
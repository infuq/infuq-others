package com.infuq.aliyun.mq;

import com.alibaba.fastjson.JSON;
import com.aliyun.mq.http.MQClient;
import com.aliyun.mq.http.MQConsumer;
import com.aliyun.mq.http.model.Message;
import org.springframework.util.CollectionUtils;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * HTTP 协议客户端接入点
 *
 */
public class AliCloudMQHTTPOrderConsumer {



    public static void main(String[] args) {

        final String host = "";
        final String instance_id = "";
        final String access_id = "";
        final String access_key = "";


        final String topic = "";
        final String group_id = "";


        MQClient mqClient = new MQClient(host, access_id, access_key);
        final MQConsumer consumer = mqClient.getConsumer(instance_id, topic, group_id, null);
        List<Message> messages = consumer.consumeMessageOrderly(3, 3);

        if ( !CollectionUtils.isEmpty(messages) ) {
            System.out.println("Receive " + messages.size() + " messages:");
            for (Message message : messages) {
                System.out.println("消息体: " + JSON.toJSONString(message));
                System.out.println("ShardingKey: " + message.getShardingKey() + ", a:" + message.getProperties().get("a"));
            }

            List<String> handles = new ArrayList<>();
            for (Message message : messages) {
                handles.add(message.getReceiptHandle());
            }
            consumer.ackMessage(handles);
        }

        mqClient.close();

        System.exit(0);


    }
}
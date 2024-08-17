#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
pip3 install kafka-python
"""

import time
from kafka import KafkaProducer
from kafka import KafkaConsumer

def producer():
    try:
        producer = KafkaProducer(bootstrap_servers=['121.196.235.63:9092'], api_version=(3,8,0))
        for i in range(2):
            msg = 'order pay success ' + str(i)
            producer.send('foo', msg.encode('utf-8'))
        producer.close()
    except Exception as e:
        print(e)

def consumer():
    consumer = KafkaConsumer('foo', group_id = 'python_consumer', bootstrap_servers = ['121.196.235.63:9092'], api_version=(3,8,0))
    for msg in consumer:
        
        print(msg)
        print("topic = %s" % msg.topic)
        print("partition = %d" % msg.offset)
        print("value = %s" % msg.value.decode())
        print("timestamp = %d" % msg.timestamp)
        print("time = ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( msg.timestamp/1000 )) )
        consumer.commit()
    

if __name__ == '__main__':
    # producer()
    consumer()
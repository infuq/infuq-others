package com.infuq.redis;

import io.netty.bootstrap.Bootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import lombok.extern.slf4j.Slf4j;
import java.net.InetSocketAddress;



@Slf4j
public class RedisOfNetty {

    public static void main(String[] args) {

        Bootstrap bootstrap = new Bootstrap();
        EventLoopGroup group = new NioEventLoopGroup();

        bootstrap.group(group)
                .channel(NioSocketChannel.class)
                .handler(new ChannelInitializer<NioSocketChannel>() {
                    @Override
                    protected void initChannel(NioSocketChannel ch) throws Exception {

                        ChannelPipeline channelPipeline = ch.pipeline();
                        channelPipeline.addLast(new StringEncoder());
                        channelPipeline.addLast(new StringDecoder());
                        channelPipeline.addLast(new ClientInHandler());

                    }
                });

        bootstrap.connect(new InetSocketAddress("127.0.0.1", 6379));

    }


}

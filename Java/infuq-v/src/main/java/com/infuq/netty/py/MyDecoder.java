package com.infuq.netty.py;


import com.alibaba.fastjson.JSON;
import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;


public class MyDecoder extends SimpleChannelInboundHandler<ByteBuf> {


    @Override
    protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) throws Exception {


        byte[] bytes = new byte[msg.readableBytes()];
        msg.readBytes(bytes);


        String json = new String(bytes, "UTF-8");

        MyModel v = JSON.parseObject(json, MyModel.class);

        ctx.fireChannelRead(v);


    }
}

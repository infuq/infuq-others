package com.infuq.netty.py;


import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;


public class ServerHandler extends SimpleChannelInboundHandler<MyModel> {


    @Override
    protected void channelRead0(ChannelHandlerContext ctx, MyModel msg) throws Exception {


        System.out.println(msg.getAddr());


    }
}

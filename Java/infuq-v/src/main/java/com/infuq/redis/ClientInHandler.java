package com.infuq.redis;

import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import lombok.extern.slf4j.Slf4j;


@Slf4j
public class ClientInHandler extends SimpleChannelInboundHandler<String> {

    private static final String CRLF = "\r\n";

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {

        String key = "k9";
        String value = "v9";

        // 2.组装命令
        StringBuilder command = new StringBuilder();

        // *<参数个数> CRLF
        String number = "*3" + CRLF;
        command.append(number);

        // $<参数字节数>CRLF<参数>CRLF
        String cmd = "$3" + CRLF + "SET" + CRLF;
        command.append(cmd);

        // $<参数字节数>CRLF<参数>CRLF
        cmd = "$" + key.getBytes().length + CRLF + key + CRLF;
        command.append(cmd);

        // $<参数字节数>CRLF<参数>CRLF
        cmd = "$" + value.getBytes().length + CRLF + value + CRLF;
        command.append(cmd);


        // 3.向服务器发送命令
        ctx.writeAndFlush(command);


    }


    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {

        System.out.println("接收到服务端的响应: " + msg);

    }
}

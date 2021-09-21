package com.infuq.redis;

import java.io.IOException;
import java.net.Socket;



public class RedisOfSocket {

    private static final String CRLF = "\r\n";

    public static void main(String[] args) throws IOException {

        String key = "k6";
        String value = "v6";

        sendCmd(key, value);

    }

    private static void sendCmd(String key, String value) throws IOException {

        // 1.建立连接
        Socket client = new Socket("127.0.0.1", 6379);



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
        client.getOutputStream().write(command.toString().getBytes());



        // 4.接收服务器响应
        byte[] response = new byte[1024];
        int c = client.getInputStream().read(response);
        System.out.println(new String(response, 0, c));

    }


}

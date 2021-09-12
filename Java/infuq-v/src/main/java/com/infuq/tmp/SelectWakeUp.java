package com.infuq.tmp;


import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.nio.channels.Selector;
import java.lang.RuntimeException;
import java.lang.Thread;
import java.nio.channels.ServerSocketChannel;

public class SelectWakeUp {

    private static final int MAXSIZE=5;

    public static final void main(String argc[]) {
        Selector [] sels = new Selector[ MAXSIZE];
        try {
            for ( int i = 0 ;i< MAXSIZE ;++i ) {
                sels[i] = Selector.open();
                //sels[i].close();
            }
            Thread.sleep(3000000);
        } catch (Exception x) {
            throw new RuntimeException(x);
        }





        ServerSocketChannel serverSocketChannel;

        Selector selector = Selector.open();
        serverSocketChannel = ServerSocketChannel.open();

        ServerSocket serverSocket = serverSocketChannel.socket();




    }

}
package com.infuq.memory;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;

public class FileChannelExample {


    public static void main(String[] args) throws FileNotFoundException {


        RandomAccessFile aFile = new RandomAccessFile("data/nio-data.txt", "rw");
        FileChannel inChannel = aFile.getChannel();

//        inChannel.map()



    }


}

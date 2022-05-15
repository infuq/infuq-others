package com.infuq.mmap;

import cn.hutool.core.util.ReflectUtil;
import java.io.File;
import java.io.RandomAccessFile;
import java.lang.reflect.Field;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;


public class MmapTest {

    public static void main(String[] args) {
        try {
            String fileName = "D:/tmp/mmap.txt";
            File file = new File(fileName);

            FileChannel fileChannel = new RandomAccessFile(file, "rw").getChannel();
            MappedByteBuffer mappedByteBuffer = fileChannel.map(FileChannel.MapMode.READ_WRITE, 0, 1024 * 64);


            Field field = ReflectUtil.getField(MappedByteBuffer.class, "address");
            field.setAccessible(true);

            try {
                long address = (long) field.get(mappedByteBuffer);
                System.out.println(address);
            } catch (IllegalAccessException ignored) {
            }



            System.out.println("yield");


        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

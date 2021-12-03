package com.infuq.memory;

import org.jctools.util.UnsafeAccess;
import org.openjdk.jol.info.ClassLayout;
import org.openjdk.jol.vm.VM;
import sun.misc.Unsafe;

import java.io.RandomAccessFile;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;

public class MapExample {



    int value;


    private MapExample() {
        this(20);
    }

    private MapExample(int value) {
        this.value = value;
    }


    public static void main(String[] args) throws Exception {

        // javac -d . -classpath ".:/usr/java/jdk1.8.0_171/jre/lib/*:./lib/*" AddressExample.java
        // java -classpath ".:/usr/java/jdk1.8.0_171/jre/lib/*:./lib/*" -Xms50M -Xmx50M -XX:MaxDirectMemorySize=32M -XX:MetaspaceSize=12M -XX:MaxMetaspaceSize=16M -XX:-UseCompressedClassPointers -XX:-UseCompressedOops com.infuq.memory.AddressExample

        // jmap -dump:format=b,file=1.hprof 9940
        // more /proc/9940/maps > maps.txt
        // more /proc/9940/smaps > smaps.txt


        /*
        -Xms50M -Xmx50M
        -XX:MaxDirectMemorySize=32M
        -XX:MetaspaceSize=12M
        -XX:MaxMetaspaceSize=16M
        -XX:-UseCompressedClassPointers -XX:-UseCompressedOops
         */

//        System.out.println(VM.current().details());

        MapExample addressExample = new MapExample();
        long heap = VM.current().addressOf(addressExample);
        System.out.println("heap address:\t 0x" + Long.toHexString(heap));

        // Class对象处在堆空间
        long clazz = VM.current().addressOf(MapExample.class);
        System.out.println("clazz address:\t 0x" + Long.toHexString(clazz));


        // 查看元空间地址
        System.out.println(ClassLayout.parseInstance(addressExample).toPrintable());
        

        // 直接内存
        Unsafe unsafe = UnsafeAccess.UNSAFE;
        long direct = unsafe.allocateMemory(33 * 1024 * 1024);
        System.out.println("direct address:\t 0x" + Long.toHexString(direct));
        byte b = 1;
        unsafe.putByte(direct, b);
        int i = 33 * 1024 * 1024;
        while (i > 0) {
            unsafe.putByte(direct, b);
            direct = direct + 1;
            i = i - 1;
        }


        RandomAccessFile f = new RandomAccessFile("D:\\tmp\\map.txt", "rw");
        FileChannel channel = f.getChannel();
        MappedByteBuffer buf = channel.map(FileChannel.MapMode.READ_WRITE, 0, 5*1024*1024);
        byte[] q = new byte[5*1024*1024];
        buf.put(q);


//        f.close();
//        channel.close();


        while (true) {

            Thread.sleep(5000);
            System.out.println(addressExample.value);
        }

    }



}

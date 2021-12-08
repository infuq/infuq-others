package com.infuq.memory;

import org.jctools.util.UnsafeAccess;
import org.openjdk.jol.info.ClassLayout;
import org.openjdk.jol.vm.VM;
import sun.misc.Unsafe;

import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
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


        MapExample _addressExample = new MapExample();
        long _heap = VM.current().addressOf(_addressExample);
        System.out.println("heap address:\t 0x" + Long.toHexString(_heap));

        // Class对象处在堆空间
        long clazz = VM.current().addressOf(MapExample.class);
        System.out.println("clazz address:\t 0x" + Long.toHexString(clazz));



        Manager manager = new Manager();
        manager.setMapExample(_addressExample);
        long __heap = VM.current().addressOf(manager);
        System.out.println("heap address:\t 0x" + Long.toHexString(__heap));



/*
        // 查看元空间地址
        System.out.println(ClassLayout.parseInstance(addressExample).toPrintable());
        

        // 直接内存 通过反射获取unsafe方式不受 -XX:MaxDirectMemorySize 参数限制
        Unsafe unsafe = org.jctools.util.UnsafeAccess.UNSAFE;
        long native_mem = unsafe.allocateMemory(33 * 1024 * 1024);
        System.out.println("direct address:\t 0x" + Long.toHexString(native_mem));
        byte b = 1;
        unsafe.putByte(native_mem, b);
        int i = 33 * 1024 * 1024;
        while (i > 0) {
            unsafe.putByte(native_mem, b);
            native_mem = native_mem + 1;
            i = i - 1;
        }


        // 最大直接内存
        System.out.println(sun.misc.VM.maxDirectMemory());

        ByteBuffer byteBuffer = ByteBuffer.allocateDirect(31 * 1024 * 1024);
        System.out.println(ClassLayout.parseInstance(byteBuffer).toPrintable());

*/

/*
        RandomAccessFile f = new RandomAccessFile("/home/v-dev/tmp/map.txt", "rw");
        FileChannel channel = f.getChannel();
        MappedByteBuffer buf = channel.map(FileChannel.MapMode.READ_WRITE, 0, 5*1024*1024);
        byte[] q = new byte[5*1024*1024];
        buf.put(q);
*/

//        f.close();
//        channel.close();

//
//        while (true) {
//
//            Thread.sleep(5000);
//            System.out.println(addressExample.value);
//        }

        System.in.read();

    }



}

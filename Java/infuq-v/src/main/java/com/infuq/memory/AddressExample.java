package com.infuq.memory;

import org.jctools.util.UnsafeAccess;
import org.openjdk.jol.info.ClassLayout;
import org.openjdk.jol.vm.VM;
import sun.misc.Unsafe;

public class AddressExample {



    int value;


    private AddressExample() {
        this(20);
    }

    private AddressExample(int value) {
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

        AddressExample addressExample = new AddressExample();
        long heap = VM.current().addressOf(addressExample);
        System.out.println("heap address:\t 0x" + Long.toHexString(heap));

        // Class对象处在堆空间
        long metaspace = VM.current().addressOf(AddressExample.class);
        System.out.println("heap address:\t 0x" + Long.toHexString(metaspace));


        // 查看元空间地址
        System.out.println(ClassLayout.parseInstance(addressExample).toPrintable());
        

        // 直接内存
        Unsafe unsafe = UnsafeAccess.UNSAFE;
        long direct = unsafe.allocateMemory(30 * 1024 * 1024);
        System.out.println("direct address:\t 0x" + Long.toHexString(direct));



        Thread.sleep(3600*1000);

    }



}

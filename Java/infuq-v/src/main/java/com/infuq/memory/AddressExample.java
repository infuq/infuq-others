package com.infuq.memory;

import org.jctools.util.UnsafeAccess;
import sun.misc.Unsafe;

public class AddressExample {


    private int value;


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
        -Xms50M -Xmx50M = 51200KB
        -XX:MaxDirectMemorySize=32M
        -XX:MetaspaceSize=12M   = 12288KB
        -XX:MaxMetaspaceSize=16M
        -XX:-UseCompressedClassPointers -XX:-UseCompressedOops
         */

        AddressExample addressExample = new AddressExample();
        long heap = location(addressExample);
        System.out.println("heap address: 0x" + Long.toHexString(heap));

        long metaspace = location(AddressExample.class);
        System.out.println("metaspace address: 0x" + Long.toHexString(metaspace));


        Unsafe unsafe = UnsafeAccess.UNSAFE;
        long direct = unsafe.allocateMemory(30 * 1024 * 1024);
        System.out.println("direct address: 0x" + Long.toHexString(direct));


//        Thread.sleep(3600*1000);

    }





    private static long location(Object object) {

        Unsafe unsafe = UnsafeAccess.UNSAFE;

        Object[] array = new Object[] {object};

        long baseOffset = unsafe.arrayBaseOffset(Object[].class);

        int addressSize = unsafe.addressSize();

        long location;

        switch (addressSize) {
            case 4:
                location = unsafe.getInt(array, baseOffset);
                break;
            case 8:
                location = unsafe.getLong(array, baseOffset);
                break;
            default:
                throw new Error("unsupported address size: " + addressSize);
        }

        return (location);

    }






}

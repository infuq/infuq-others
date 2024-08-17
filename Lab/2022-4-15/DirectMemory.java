package com.infuq.memory;

import org.jctools.util.UnsafeAccess;
import sun.misc.Unsafe;
import org.openjdk.jol.info.ClassLayout;
import org.openjdk.jol.vm.VM;
import java.util.Scanner;


public class DirectMemory {

    public static void main(String[] args) throws Exception {


        Object obj = new Object();
        long heap = VM.current().addressOf(obj);
        System.out.println("heap address:\t 0x" + Long.toHexString(heap));


        Scanner scanner = new Scanner(System.in);

        long _30M = 30 * 1024 * 1024;

        long direct = 0;
        Unsafe unsafe = UnsafeAccess.UNSAFE;
        while (scanner.hasNext()) {
            String input = scanner.next();
            
            if (input.equals("1")) {
                System.out.println("malloc...");
                direct = unsafe.allocateMemory(_30M);
            }
            else if (input.equals("2")) {
                System.out.println("init...");
                byte b = 6;
                unsafe.setMemory(direct, _30M, b);
            }
        }




    }



}


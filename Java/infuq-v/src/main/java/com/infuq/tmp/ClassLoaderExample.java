package com.infuq.tmp;

import java.util.Scanner;

public class ClassLoaderExample {


    public static void main(String[] args) throws Exception {

        Scanner scanner = new Scanner(System.in);

        /*
         * 从命令行读取指定扫描的路径
         * 例如
         * Unix : /usr/bin/
         * Windows : D:\\repository\\class
         */
        String scanPath = scanner.next();
        MyClassLoader myClassLoader = new MyClassLoader(scanPath);

        /*
         * 读取类的全限定名 , 例如 java.lang.Object
         *
         */
        String packageNamePath = scanner.next();


        Class<?> clazz = myClassLoader.loadClass(packageNamePath);
        if (clazz != null)
            System.out.println(packageNamePath + "的类加载器是:" + clazz.getClassLoader());

        System.out.println("系统类加载器扫描文件路径:" + System.getProperty("java.class.path"));




    }


}

package com.infuq;

import java.util.Scanner;

public class Example {

    public static void main(String[] args) throws Exception {

        System.out.print("请输入类加载的路径: ");
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
         * 读取类的全限定名, 例如 java.lang.Object
         *
         */
        System.out.print("请输入待加载的类全限定名称: ");
        String packageNamePath = scanner.next();


        System.out.println();
        Class<?> clazz = myClassLoader.loadClass(packageNamePath);
        if (clazz != null)
            System.out.println(packageNamePath + "类加载器是: " + clazz.getClassLoader());
        
        System.out.println("系统类加载器扫描文件路径: " + System.getProperty("java.class.path"));

        // 不让进程退出. 使用Arthas工具连接目标JVM, 使用classloader命令查看一些信息
        System.in.read();


    }

}

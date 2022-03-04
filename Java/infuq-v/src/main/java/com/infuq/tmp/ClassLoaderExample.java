package com.infuq.tmp;

import java.lang.reflect.Method;
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

        boolean resolve = false;
        if (resolve) {

            Method method = ClassLoader.class.getDeclaredMethod("loadClass", String.class, boolean.class);
            method.setAccessible(true);
            Object clazz = method.invoke(myClassLoader, packageNamePath, Boolean.TRUE);

            if (clazz != null)
                System.out.println(packageNamePath + "的类加载器是:" + ((Class<?>)clazz).getClassLoader());
        }
        else {
            Class<?> clazz = myClassLoader.loadClass(packageNamePath);
            if (clazz != null)
                System.out.println(packageNamePath + "的类加载器是:" + clazz.getClassLoader());

            clazz.newInstance();
        }


        System.out.println("系统类加载器扫描文件路径:" + System.getProperty("java.class.path"));

        // 不让进程退出. 使用Arthas工具连接目标JVM, 使用classloader命令查看一些信息
        System.in.read();





    }


}

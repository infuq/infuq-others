package com.infuq.memory;

import com.google.common.collect.Lists;
import groovy.lang.GroovyClassLoader;

import java.lang.reflect.Method;
import java.nio.ByteBuffer;
import java.util.List;

public class DirectMemExample {

    private static List<Class<?>> list = Lists.newArrayList();

    public static void main(String[] args) throws Exception {


/*
-Xms50M
-Xmx50M
-XX:MaxDirectMemorySize=32M
-XX:MetaspaceSize=12M
-XX:MaxMetaspaceSize=16M
-XX:-UseCompressedClassPointers
-XX:-UseCompressedOops
*/

        Object obj = new Object();


        ByteBuffer.allocateDirect(1024);

        int i = 1;

        for(;;) {

            try {
                compile(i);
                Thread.sleep(3000);
            } catch (Exception ignored) {}
            i = i + 1;

        }
    }


    private static void compile(int index) throws Exception {

        GroovyClassLoader groovyClassLoader = new GroovyClassLoader();
        Class<?> clazz = groovyClassLoader.parseClass("package com.infuq.memory;\n" +
                "\n" +
                "public class Main"+ index +" {\n" +
                "\n" +
                "    public int age = 22;\n" +
                "}\n");
        System.out.println(index);
        list.add(clazz);
        /*
        Object obj = clazz.newInstance();
        Method method = clazz.getDeclaredMethod("sayHello");
        method.invoke(obj);

        Object val = method.getDefaultValue();
        System.out.println(val);
        */
    }





}

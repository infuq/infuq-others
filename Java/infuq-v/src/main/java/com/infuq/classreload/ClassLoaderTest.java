package com.infuq.classreload;

public class ClassLoaderTest {



    public static void main(String[] args) throws Exception {

        MyClassLoader myClassLoader = new MyClassLoader();

        while (true) {
            Class<?> clazz = myClassLoader.loadClass("com.infuq.Example");
            clazz.newInstance();

        }


    }


}

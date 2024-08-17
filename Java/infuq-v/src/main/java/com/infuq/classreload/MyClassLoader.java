package com.infuq.classreload;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.security.SecureClassLoader;
import java.util.HashMap;
import java.util.Map;

/*
 *
 * 未考虑并发情况
 *
 */
public class MyClassLoader extends SecureClassLoader {

    private String pathname = "D:/Repository/infuq-java/infuq-v/target/classes/";

    private static final Map<String/* 类全路径名称 */, Long/* class文件最后一次被修改时间 */> clazzFileLastModified = new HashMap<>();
    private static final Map<String/* 类全路径名称 */, Class<?>> clazzCache = new HashMap<>();

    @Override
    public Class<?> loadClass(String name) throws ClassNotFoundException {

        File file = new File(pathname + name.replaceAll("\\.", "/") + ".class");

        Class<?> clazz;

        Long cacheLastModified = clazzFileLastModified.get(name);
        long lastModified = file.lastModified();

        // class文件被修改
        if (cacheLastModified != null && lastModified != cacheLastModified) {
            try {
                clazz = new MyClassLoader().findClass(name);
                if (clazz != null) {
                    clazzCache.put(name, clazz);
                    clazzFileLastModified.put(name, file.lastModified());
                } else {
                    // 虽然文件被修改, 但是文件还在写入过程, 因此可能获取到的clazz == null
                    clazz = clazzCache.get(name);
                }
            } catch (Throwable t) {
                // 虽然文件被修改, 但是文件还在写入过程, 因此可能获取过程抛出异常
                clazz = clazzCache.get(name);
            }
        }
        // 第一次类加载或者class文件没有被修改
        else {
            // 先从缓存中获取
            clazz = clazzCache.get(name);
            if (clazz == null) {
                // 第一次类加载
                clazz = super.loadClass(name);
                if (clazz != null) {
                    clazzCache.put(name, clazz);
                    clazzFileLastModified.put(name, file.lastModified());
                }
            }
        }
        return clazz;
    }

    @Override
    public Class<?> findClass(String name) {
        try {
            byte[] b = loadClassData(name);
            if ( b != null ) {
                return defineClass(name, b, 0, b.length);
            }
        } catch (Exception ignored) { }

        return null;
    }

    private byte[] loadClassData(String name) {

        try {


            File file = new File(pathname + name.replaceAll("\\.", "/") + ".class");

            FileInputStream input = new FileInputStream(file);
            ByteArrayOutputStream out = new ByteArrayOutputStream();

            int b;
            while ((b = input.read()) != -1) {
                out.write(b);
            }

            byte[] res = out.toByteArray();

            input.close();
            out.close();

            return res;
        } catch (Exception ignored) { }

        return null;
    }

}

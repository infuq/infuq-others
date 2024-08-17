package com.infuq.tmp;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

/**
 * 自定义类加载器
 *
 * 加载指定路径的类文件
 *
 */
public class MyClassLoader extends ClassLoader {

    // MyClassLoader可以扫描的路径. 例如: /usr/include
    private final String scanPath ;


    public MyClassLoader(String scanPath){
        super();
        this.scanPath = scanPath;
    }


    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {

        byte[] classData = readFileData(name);

        if (classData != null) {
            return this.defineClass(name, classData, 0, classData.length);
        }

        return null;
    }


    // 读取clazzName对应的文件内容, 返回字节数组
    private byte[] readFileData(String clazzName) {

        File file;

        /*
         * 假如scanPath=/usr/include
         * 由于入参clazzName是类的全限定名, 例如java.lang.Object
         * 为了读取clazzName对应的文件, 需要将字符串`java.lang.Object`转成`java/lang/Object`
         * 最后得到完整文件路径/usr/include/java/lang/Object.class
         */
        if (System.getProperty("os.name").contains("Windows")) {
            clazzName = clazzName.replace(".", "\\");
            file = new File(scanPath + "\\" + clazzName + ".class");
        }
        else {
            clazzName = clazzName.replace(".", "/");
            file = new File(scanPath + "/" + clazzName + ".class");
        }


        // 读取
        if (file.exists()) {
            FileInputStream in = null;
            ByteArrayOutputStream out;
            try {
                in = new FileInputStream(file);
                out = new ByteArrayOutputStream();

                byte[] buffer = new byte[1024];
                int size;
                while ((size = in.read(buffer)) != -1) {
                    out.write(buffer, 0, size);
                }

                return out.toByteArray();
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (in != null) {
                        in.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        return null;

    }
}

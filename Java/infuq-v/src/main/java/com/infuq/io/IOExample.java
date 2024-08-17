package com.infuq.io;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.RandomAccessFile;
import java.nio.charset.StandardCharsets;

public class IOExample {


    public static void main(String[] args) throws Exception {

//        basic();

//        buffer();

        random();

    }


    public static void random() throws Exception {

        String path = "./t.txt";

        RandomAccessFile randomFile = new RandomAccessFile(path, "rw");

        randomFile.write("https://www.infuq.com".getBytes(StandardCharsets.UTF_8));
        randomFile.write("https://infuq.github.io".getBytes(StandardCharsets.UTF_8));


        Thread.sleep(300 * 1000);


        randomFile.close();




    }



    public static void buffer() throws Exception {
        String path = "./t.txt";
        File file = new File(path);

        FileOutputStream out = new FileOutputStream(file);
        BufferedOutputStream _out = new BufferedOutputStream(out);

        _out.write("www.infuq.com".getBytes(StandardCharsets.UTF_8));
        _out.write("infuq.github.io".getBytes(StandardCharsets.UTF_8));

        _out.close();
        out.close();



    }

    // 常规写方式
    public static void basic() throws Exception {
        String path = "./t.txt";
        File file = new File(path);

        FileOutputStream out = new FileOutputStream(file);

        out.write("www.infuq.com".getBytes(StandardCharsets.UTF_8));
        out.write("infuq.github.io".getBytes(StandardCharsets.UTF_8));

        out.close();

    }





}

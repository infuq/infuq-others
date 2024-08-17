package com.infuq.jute;

import org.apache.jute.BinaryInputArchive;
import org.apache.jute.BinaryOutputArchive;

import java.io.*;

public class JuteExample {

    public static void main(String[] args) throws Exception {

        serialize();

        deserizlize();


    }


    public static void deserizlize() throws Exception {
        String path = "jute.txt";
        InputStream intputStream = new FileInputStream(new File(path));



        BinaryInputArchive archive = BinaryInputArchive.getArchive(intputStream);
        // tag的名字并不重要, 读取的顺序才是核心
        System.out.println(archive.readString("name"));
        System.out.println(archive.readInt("name"));
        System.out.println(archive.readFloat("name"));
        System.out.println(archive.readBool("name"));
    }

    public static void serialize() throws Exception {

        Student stu = new Student("Libai", 23, 103.2F, true);

        String path = "jute.txt";
        OutputStream outputStream = new FileOutputStream(new File(path));


        BinaryOutputArchive archive = BinaryOutputArchive.getArchive(outputStream);
        // tag的名字并不重要
        archive.writeString(stu.getName(), "name");
        archive.writeInt(stu.getAge(), "age");
        archive.writeFloat(stu.getHeight(), "height");
        archive.writeBool(stu.getSex(), "sex");

        outputStream.flush();
        outputStream.close();

    }




}

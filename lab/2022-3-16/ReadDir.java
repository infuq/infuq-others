package com.infuq;

import java.io.File;

public class ReadDir {

    public static void main(String[] args) throws Exception {

        File file = new File("/root/2022-3-16");
        String[] files = file.list();
        for (String fileName : files) {
            System.out.println(fileName);
        }

    }

}


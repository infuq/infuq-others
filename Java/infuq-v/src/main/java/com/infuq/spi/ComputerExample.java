package com.infuq.spi;

import java.io.IOException;
import java.sql.Driver;
import java.sql.DriverManager;
import java.util.Enumeration;
import java.util.Iterator;
import java.util.ServiceLoader;

public class ComputerExample {


    public static void main(String[] args) throws Exception {


        Enumeration<Driver> drivers = DriverManager.getDrivers();

//        Class.forName("java.sql.DriverManager");


/*

        ServiceLoader<Computer> serviceLoader = ServiceLoader.load(Computer.class);

        Iterator<Computer> iterator = serviceLoader.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next().getName());
        }

        System.in.read();
*/

    }


}

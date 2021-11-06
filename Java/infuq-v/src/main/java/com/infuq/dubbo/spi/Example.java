package com.infuq.dubbo.spi;


import com.alibaba.dubbo.common.extension.ExtensionLoader;

public class Example {


    public static void main(String[] args) throws Exception {

        ExtensionLoader<Computer> extensionLoader = ExtensionLoader.getExtensionLoader(Computer.class);

        extensionLoader.getAdaptiveExtension();

        Computer dell = extensionLoader.getExtension("dell");
        System.out.println(dell.getName());

        Thread.sleep(60000);

        Computer hp = extensionLoader.getExtension("hp");
        System.out.println(hp.getName());

        System.in.read();

    }

}

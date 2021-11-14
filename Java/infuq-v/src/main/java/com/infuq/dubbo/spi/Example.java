package com.infuq.dubbo.spi;


import com.alibaba.dubbo.common.extension.ExtensionLoader;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Example {


    public static void main(String[] args) throws Exception {

        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");

//        SpringBean springBean = context.getBean("springBean", SpringBean.class);
//        System.out.println(springBean.getColor());

        ExtensionLoader<Computer> extensionLoader = ExtensionLoader.getExtensionLoader(Computer.class);

        extensionLoader.getAdaptiveExtension();

        Computer dell = extensionLoader.getExtension("dell");
        System.out.println(dell.getName());


        Computer hp = extensionLoader.getExtension("hp1");
        System.out.println(hp.getName());


    }

}

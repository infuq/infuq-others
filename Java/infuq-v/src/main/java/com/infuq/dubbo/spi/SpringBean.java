package com.infuq.dubbo.spi;

import org.springframework.stereotype.Component;

@Component
public class SpringBean {

    private static String color = "红色";

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        SpringBean.color = color;
    }
}

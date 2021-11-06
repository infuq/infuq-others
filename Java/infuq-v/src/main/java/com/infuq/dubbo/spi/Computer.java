package com.infuq.dubbo.spi;


import com.alibaba.dubbo.common.URL;
import com.alibaba.dubbo.common.extension.Adaptive;
import com.alibaba.dubbo.common.extension.SPI;

//@SPI(value = "hp")
@SPI
public interface Computer {



    String getName();


    @Adaptive
    String getAddress(URL url);

}

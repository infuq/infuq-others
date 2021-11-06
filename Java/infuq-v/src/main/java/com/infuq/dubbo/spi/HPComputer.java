package com.infuq.dubbo.spi;


import com.alibaba.dubbo.common.Extension;
import com.alibaba.dubbo.common.URL;

@Extension(value = "hp1,hp2")
public class HPComputer implements Computer {


    @Override
    public String getName() {
        return "惠普电脑";
    }

    @Override
    public String getAddress(URL url) {
        return "惠普地址";
    }


}

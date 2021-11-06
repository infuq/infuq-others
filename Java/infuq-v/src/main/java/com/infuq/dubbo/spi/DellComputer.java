package com.infuq.dubbo.spi;

import com.alibaba.dubbo.common.URL;

public class DellComputer implements Computer {
    @Override
    public String getName() {
        return "戴尔电脑";
    }

    @Override
    public String getAddress(URL url) {
        return "戴尔地址";
    }
}

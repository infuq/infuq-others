package com.infuq.dubbo.spi;

import com.alibaba.dubbo.common.URL;

public class HPWrapperComputer implements Computer {

    private Computer computer;

    public HPWrapperComputer(Computer computer) {
        this.computer = computer;
    }

    @Override
    public String getName() {
        return "包装类:" + computer.getName();
    }

    @Override
    public String getAddress(URL url) {
        return "包装类:" + computer.getAddress(url);
    }
}

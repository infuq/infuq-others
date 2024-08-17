package com.infuq.dubbo.spi;
import com.alibaba.dubbo.common.extension.ExtensionLoader;

public class Computer$Adaptive implements com.infuq.dubbo.spi.Computer {
    public String getAddress(com.alibaba.dubbo.common.URL arg0) {
        if (arg0 == null)
            throw new IllegalArgumentException("url == null");

        com.alibaba.dubbo.common.URL url = arg0;
        String extName = url.getParameter("computer");
        if(extName == null)
            throw new IllegalStateException("Fail to get extension(com.infuq.Computer) name from url(" + url.toString() + ") use keys([computer])");
        com.infuq.dubbo.spi.Computer extension = (com.infuq.dubbo.spi.Computer)ExtensionLoader.getExtensionLoader(com.infuq.dubbo.spi.Computer.class).getExtension(extName);
        return extension.getAddress(arg0);
    }
    public String getName() {throw new UnsupportedOperationException("method public abstract java.lang.String com.infuq.Computer.getName() of interface com.infuq.Computer is not adaptive method!");
    }
}

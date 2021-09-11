package com.infuq.tmp;

import com.sun.tools.attach.VirtualMachine;
import sun.tools.attach.HotSpotVirtualMachine;

import java.io.InputStream;

public class Attach {

    public static void main(String[] args)throws Exception {
        VirtualMachine virtualMachine = VirtualMachine.attach("6361");
        HotSpotVirtualMachine hotSpotVirtualMachine = (HotSpotVirtualMachine)virtualMachine;
        InputStream inputStream = hotSpotVirtualMachine.remoteDataDump(new String[]{});

        byte[] buff = new byte[256];
        int len;
        do {
            len = inputStream.read(buff);
            if (len > 0) {
                String respone = new String(buff, 0, len, "UTF-8");
                System.out.print(respone);
            }
        } while(len > 0);

        inputStream.close();
        virtualMachine.detach();
    }
}

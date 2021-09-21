package com.infuq.tmp;

import java.util.logging.Logger;

public class Main {
    
    public static void main(String args[]) {
                
        Logger.getLogger("com.infuq.tmp.Main").info("Java");


        for (;;) {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

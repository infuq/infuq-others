package com.infuq.netty.py;

import lombok.Data;

import java.io.Serializable;

@Data
public class MyModel implements Serializable {

    private Integer year;
    private String addr;

}

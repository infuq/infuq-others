package com.infuq.tmp;

import java.util.HashMap;

// https://leetcode-cn.com/problems/first-unique-character-in-a-string/

public class FirstUniqueCharacter {

    public static void main(String[] args) {

        String data = "AGFHOGHIRFEAOIIFD";

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0; i < data.length(); i++) {

            char c = data.charAt(i);
            Integer value = map.get(c);
            if (value == null) {
                map.put(c, 1);
            } else {
                map.put(c, value + 1);
            }
        }


        for (int i = 0; i < data.length(); i++) {
            char c = data.charAt(i);
            if (map.get(c) == 1) {
                System.out.println(i);
                break;
            }
        }


    }

}
package com.infuq;

import java.util.ArrayList;


public class Triangle {

    public static void main(String[] args) {

        ArrayList<ArrayList<Integer>> triangle = new ArrayList<ArrayList<Integer>>();

        // init
        ArrayList<Integer> l0 = new ArrayList<>();
        l0.add(2);
        ArrayList<Integer> l1 = new ArrayList<>();
        l1.add(3);
        l1.add(4);
        ArrayList<Integer> l2 = new ArrayList<>();
        l2.add(6);
        l2.add(5);
        l2.add(7);
        ArrayList<Integer> l3 = new ArrayList<>();
        l3.add(4);
        l3.add(1);
        l3.add(8);
        l3.add(3);


        triangle.add(l0);
        triangle.add(l1);
        triangle.add(l2);
        triangle.add(l3);

        System.out.println(minimumTotal(triangle));


    }

    public static int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {




        if (triangle.isEmpty())
            return 0;
        if (triangle.size() == 1)
            return triangle.get(0).get(0);

        /*
         *
         *
         * [
         *     [2]
         *    [3,4]
         *   [6,5,7]
         *  [4,1,8,3]
         * ]
         *
         */

        int [][] dp = new int[triangle.size()][triangle.get(triangle.size()-1).size()];

        // Bottom level initialization
        for (int i = 0; i < triangle.get(triangle.size() - 1).size(); i++)
            dp[triangle.size() - 1][i] = triangle.get(triangle.size() - 1).get(i);

        // From the last second line to the top line
        for (int i = triangle.size() - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = Math.min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle.get(i).get(j);
            }
        }

        return dp[0][0];
    }
}
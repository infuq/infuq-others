package com.infuq;

import org.junit.Test;

import java.util.Arrays;
import java.util.Stack;


public class ExampleTest {

    private static int j = 0;
    private static int[] arr = new int[200];

    @Test
    public void t1() {

        long start = System.currentTimeMillis();
        int i = fib(10);
        System.out.println(i);
        System.out.println(j);
        long end = System.currentTimeMillis();
        System.out.println( (end - start) );
    }

    private int fib(int n) {
        j = j + 1;
        if (n == 0)
            return 0;

        if (n == 1)
            return 1;

        if (arr[n] == 0)
            arr[n] = fib(n - 1) + fib(n - 2);
        return arr[n];

    }



    private static Stack<Integer> stack = new Stack<>();
    @Test
    public void t2() {

        int n = 10;
        f(5, stack);

    }

    private void f(int n, Stack<Integer> stack) {
        if (n == 1) {
            stack.push(n);
            System.out.println(stack);
            stack.pop();
            return ;
        }


        for (int i = 1; i < n; i++) {
            // i + (n-i)
            stack.push(i);
            if (n == 5)
                System.out.println(Arrays.asList(i, n-i));
            f(n-i, stack);
            stack.pop();
        }


    }








}

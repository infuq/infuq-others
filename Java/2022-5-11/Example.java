
package com.infuq;

import java.util.Stack;


/**
 * 穷举 ["A","B","C"] 所有组合
 * 所有组合如下: ["A"],["B"],["C"],["A","B"],["A","C"],["B","C"],["A","B","C"] 共7种
 *  
 */
public class Example {

    public static void main(String[] args) {

        String[] arr = { "A", "B", "C" };
        Stack<String> stack = new Stack<>();

        f(arr, 0, arr.length - 1, stack);
    }

    private static void f(String[] arr, int left, int right, Stack<String> stack) {
        if (arr.length == 1) {
            stack.push(arr[left]);
            System.out.println(stack);
            return ;
        }

        for (int i = left; i <= right; i++) {
            stack.push(arr[i]);
            System.out.println(stack);

            // 递归
            f(arr, i + 1, right, stack);

            stack.pop();
        }
    }

}

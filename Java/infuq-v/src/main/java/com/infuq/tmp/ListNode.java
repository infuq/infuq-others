package com.infuq.tmp;

public class ListNode {

    private static int year = 2022;

    static {
        System.out.println("ListNode静态代码块");
    }

    private int data;
    private ListNode next;

    public ListNode() {}

    public ListNode(int data) {
        this.data = data;
        this.next = null;
    }

    public void setData(int data) {
        this.data = data;
    }

    public void setNext(ListNode next) {
        this.next = next;
    }

    public int getData() {
        return this.data;
    }

    public ListNode getNext() {
        return this.next;
    }

}
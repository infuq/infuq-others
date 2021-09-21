package com.infuq.tmp;

public class ListNode {

    private int data;
    private ListNode next;

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
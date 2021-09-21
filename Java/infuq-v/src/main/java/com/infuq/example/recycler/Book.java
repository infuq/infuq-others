package com.infuq.example.recycler;


import io.netty.util.Recycler;

public class Book {

    private String name;

    private final Recycler.Handle<Book> recyclerHandle;

    Book(Recycler.Handle<Book> recyclerHandle) {
        this.recyclerHandle = recyclerHandle;
    }

    public void setName(String name) {
        this.name = name;
    }

    void recycle() {
        recyclerHandle.recycle(this);
    }

}

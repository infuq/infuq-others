package com.infuq.spring;

import org.springframework.beans.factory.FactoryBean;

public class BookFactoryBean implements FactoryBean<Book> {

    @Override
    public Book getObject() throws Exception {
        return new Book();
    }

    @Override
    public Class<?> getObjectType() {
        return Book.class;
    }

}

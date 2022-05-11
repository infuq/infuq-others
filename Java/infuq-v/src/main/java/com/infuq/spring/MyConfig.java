package com.infuq.spring;


import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@ComponentScan({"com.infuq.spring"})
@Configuration
public class MyConfig {

    @Bean
    public BookFactoryBean bookFactoryBean() {
        return new BookFactoryBean();
    }

}

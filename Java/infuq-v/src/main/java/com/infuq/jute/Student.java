package com.infuq.jute;

public class Student {

    private String name;
    private int age;
    private Float height;
    private Boolean sex;

    public Student() {}

    public Student(String name, int age, Float height, Boolean sex) {
        this.name = name;
        this.age = age;
        this.height = height;
        this.sex = sex;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Float getHeight() {
        return height;
    }

    public void setHeight(Float height) {
        this.height = height;
    }

    public Boolean getSex() {
        return sex;
    }

    public void setSex(Boolean sex) {
        this.sex = sex;
    }
}

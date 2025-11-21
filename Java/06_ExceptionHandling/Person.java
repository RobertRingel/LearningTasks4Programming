package org.htwd.pool.o6;

public class Person {
    private String name;
    private final String birthDay;

    public Person(String name, String bday) {
        this.name = name;
        this.birthDay = bday;
    }

    public String getName() { return this.name; }
    public String getBirthDay() { return this.birthDay; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append(" : ");
        sb.append(this.getBirthDay());
        return sb.toString();
    }

    public static void main(String[] args) {
        Person max = new Person("Max", "07.11/2002");
        System.out.println(max);
    }
}

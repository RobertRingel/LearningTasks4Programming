package org.htwd.pool.o3;

public class Person {
    private String name;
    private final String BIRTH_DAY;

    public Person(String name, String bday) {
        this.name = name;
        this.BIRTH_DAY = bday;
    }

    public String getName() { return this.name; }
    public String getBirthDay() { return this.BIRTH_DAY; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append(" : ");
        sb.append(this.getBirthDay());
        return sb.toString();
    }

    public static void main(String[] args) {
        Person max = new Person("Max", "07/11/2002");
        System.out.println(max);
    }
}

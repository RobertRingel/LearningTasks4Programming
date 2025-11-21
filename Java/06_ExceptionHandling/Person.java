package org.htwd.pool.o6;

import java.util.regex.Pattern;

public class Person {
    private String name;
    private final String birthDay;

    public Person(String name, String bday) throws IllegalArgumentException {
        if (name == null || name=="")
            throw new IllegalArgumentException("Invalid parameter for name");
        // Pattern.matches: perform basic date format check: DD/MM/YYYY
        if (bday == null || Pattern.matches("^\\d{2}[/-]\\d{2}[/-][012]\\d{3}$", bday) == false)
            throw new IllegalArgumentException("Invalid parameter for bday");
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
        try {
            Person max = new Person("Max", "07.11/2002");
            System.out.println(max);
        } catch (IllegalArgumentException e) {
            System.out.println("There is a problem: "+e.getMessage());
        }
        System.out.println("regular end of the program");
    }
}

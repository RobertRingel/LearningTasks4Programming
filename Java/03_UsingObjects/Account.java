package org.htwd.pool.o3;

public class Account {
    private final String iban;
    private Person person;
    private double balance;

    public Account(String iban, Person person) {
        this.iban = iban;
        this.person = person;
        this.balance = 0.0;
    }

    public Account(String iban, String name, String bday) {
        this.iban = iban;
        this.person = new Person(name, bday);
        this.balance = 0.0;
    }

    public void account(double amount) {
        this.balance += amount;
    }

    public double getBalance() {
        return this.balance;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.iban);
        sb.append(" : ");
        sb.append(this.person);
        sb.append(" : EUR:");
        sb.append(this.balance);
        return sb.toString();
    }

    public static void main(String[] args) {
        Person max = new Person("Max", "07/11/2002");
        Account acc_max = new Account("DE123454322134", max);
        acc_max.account(45.00);
        System.out.println(acc_max);
    }
}
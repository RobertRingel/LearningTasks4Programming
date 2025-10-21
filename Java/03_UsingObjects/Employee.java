package org.htwd.pool.o3; 

public class Employee {
    private Person person;
    private Account account;
    private String job;
    private double salary;

    public Employee(Person person, Account account) {
        this.person = person;
        this.account = account;
        this.job = "undef";
        this.salary = 0.0;
    }

    public String getName() { return this.person.getName(); }
    public void paySalary() { this.account.account(this.salary); }
    public void setJob(String job) { this.job = job; }
    public void setSalary(double salary) { this.salary = salary; }

    public String getBadge() {
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append("\n");
        sb.append(this.job);
        return sb.toString();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.person.toString());
        sb.append(" : ");
        sb.append(this.job);
        sb.append(" : salary EUR:");
        sb.append(this.salary);
        sb.append(" : account:");
        sb.append(this.account);
        return sb.toString();
    }

    public static void main(String[] args) {
        Person bob = new Person("Bob", "27/12/2002");
        Account acc_bob = new Account("DE123454322134", bob);
        Employee eBob = new Employee(bob, acc_bob);
        eBob.setJob("Manager");
        eBob.setSalary(5000.0);
        System.out.println(eBob.getBadge());
        System.out.println("---------------------------");
        System.out.println(eBob);
    }
}

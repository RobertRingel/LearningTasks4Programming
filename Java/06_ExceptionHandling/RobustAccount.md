Topic: exception handling

## Learning Task: Improve the account robustness!

The following Java code represents another bank account that makes use of the [Person class](Person.java).  

Read the code carfully and run it. Identify weaknesses in the given implementation. Change the implementation in a way to make it more robust. The code shall check whether the given IBAN is a valid German IBAN. It shall identify invalid date strings and missing person names. Furthermore it shall reject account operations causing a negative balance.  
The code improvements shall make use of the approriate Exception-objects to get thrown in the related situations.

``` java
package org.htwd.pool.o6;

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
``` 
**Java regular expressions to check IBAN and date**
``` java
German IBAN: DE + 20 digits 
regex: Pattern.matches("^DE\\d{20}$", iban)

basic date check 
regex: Pattern.matches("^\\d{2}[/-]\\d{2}[/-][012]\\d{3}$", bday)
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

import java.util.regex.Pattern;

public class Account {
    private final String iban;
    private Person person;
    private double balance;

    public Account(String iban, Person person) throws NullPointerException, IllegalArgumentException {
        if (person == null)
            throw new NullPointerException("parameter Person is null");
        if (Pattern.matches("^DE\\d{20}$", iban) == false)
            throw new IllegalArgumentException("given IBAN is not a valid German IBAN");
        this.iban = iban;
        this.person = person;
        this.balance = 0.0;
    }

    public Account(String iban, String name, String bday) throws IllegalArgumentException {
        if (Pattern.matches("^DE\\d{20}$", iban) == false)
            throw new IllegalArgumentException("given IBAN is not a valid German IBAN");
        if (name==null || name=="")
            throw new IllegalArgumentException("name was found empty");
        if (bday == null || Pattern.matches("^\\d{2}[/-]\\d{2}[/-][012]\\d{3}$", bday) == false)
            throw new IllegalArgumentException("Invalid parameter for bday");
        this.iban = iban;
        this.person = new Person(name, bday);
        this.balance = 0.0;
    }

    public void account(double amount) throws RuntimeException {
        if (this.balance+amount < 0.0)
            throw new RuntimeException("insufficient funds in the account");
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
        Account acc_max = new Account("DE12345678901234567890", max);
        acc_max.account(45.00);
        System.out.println(acc_max);
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | completion task | 2 - normal     | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
uob-1: basics of creating and using objects  
exc-1: basics of exception-handling

#### Learning Activities

1) read and run the given Java code
2) identify weaknesses in the given code   
3) implement the required checks and throw related exceptions    
4) test the improved implementation by appropritate method-calls in the main-method  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.:  
Chapter 5, pages 135-156 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

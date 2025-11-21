Topic: exception handling

## Learning Task: Tighten your class!

Given is the Account-Java-class. The implementation performs various checks to make sure only valid data will be stored in the class attributes. In case of invalid data the class will throw related exceptions.

Read the code and understand the concepts used to handle invalid data. Implement similar checks in any of your own classes in order to tighten it against invalid or corrupt data. Focus on the constructor, the setter-methods and calculations that can crash or yield invalid results.  

Discuss and demonstrate the improvements you made in your own class to another student.

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

---------------------------------------

### Solution

... any Java code similar to the sample implementation shown above.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | imitation task  | 2 - normal     | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
uob-1: basics of creating and using objects  
exc-1: basics of exception-handling

#### Learning Activities

1) read the given Java code in order to identify the concepts to handle invalid data  
2) implement the same concepts into a self written Java class to tighten the implementation     
3) test the improved implementation by appropriate method-calls in the main-method  
4) demonstrate the resulting and improved class to another student  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
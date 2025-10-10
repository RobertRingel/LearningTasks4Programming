Topic: using objects

## Learning Task: Voucher for a Person 

The code below shows the Person-class. Implement a Voucher-class that that uses Person-objects to relate the voucher to a certein person. The Voucher-class might imitate the Account-class given below.  

Implement a main-method to demonstrate the features of the person-related voucher.

**The Person class:**
``` java
package org.htwd.pool.o3;

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
}
```

*Note:* For the sake of simplicity the birthday's date is modelled by a string instead of a date object.

**The Account class:**
``` java
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
```

---------------------------------------

### Solution
 
``` java
package org.htwd.pool.o3;

public class Voucher {
    static protected final double DEFAULT_VALUE = 100.0;
    private final String ID;
    private double currentValue;
    private Person person;

    public Voucher(String id, Person person) {
        this.currentValue = Voucher.DEFAULT_VALUE;
        this.ID = id;
        this.person = person;
    }

    public boolean consume(double amount) {
        if ((amount < 0.0) || ((this.currentValue-amount) < 0.0))
            return false;
        this.currentValue = this.currentValue - amount;
        return true;
    }

    public Person getPerson() { return this.person; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.getPerson());
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }

    public static void main(String args[]) {
        Person liz = new Person("Liz", "27/01/2002");
        Voucher v = new Voucher("abc123", liz);
        v.consume(10.0);
        System.out.println(v);
        v.consume(310.0);
        System.out.println(v);
    }
}
``` 


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand concepts of using objects             | imitation task  | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  

#### Learning Activities

1) read the Java of the Person and Account-class code
2) develop ideas of a Voucher-class
3) implement the Voucher-class similar to the Account-class
4) test the code with help of a main-method

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - Classes and objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  
[tutorialspoint.com: Java - Composition](https://www.tutorialspoint.com/association-composition-and-aggregation-in-java)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

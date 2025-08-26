Topic: classes, modifiers

## Learning Task: Check the Account class

The Java code below implements a basic bank account. Read the code to obtain an understandig. Implement a main-method to demonstrate the usage of this class. 

Is there a way to make sure, the limit value of account will not be changed?

Finally, do you see any problem in the Account-class?

``` java
package org.htwd.pool.o1;

import java.lang.Math;

public class Account {

    private String number;
    private double balance;
    private double limit;
    private String name;

    public Account(String name, String number) {
        this.number = number;
        this.balance = 0.0;
        this.limit = 1000.0;
        this.name = name;
    }

    private boolean checkAmount(double amount) {
        if (Math.abs(amount) > this.limit)
            return false;
        if ((this.balance + amount) < 0)
            return false;
        return true;
    }

    public boolean bookEntry(double amount) {
        if (checkAmount(amount) == true) {
            this.balance = this.balance + amount;
            return true;
        }
        return false;
    }

    public double getBalance() {
        return this.balance;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : ");
        sb.append(this.number);
        sb.append(" : ");
        sb.append(this.balance);
        return sb.toString();
    }

}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o1;

import java.lang.Math;

public class Account {
    
    // final: limit can only be set once e.g. in the constructor
    private final double limit;  

...

public static void main(String[] args) {
        Account a = new Account("Robert", "123-R");
        System.out.println(a.toString());
        a.bookEntry(152.10);
        double b = a.getBalance();
        System.out.println(b);
        a.bookEntry(-100.00);
        System.out.println(a.toString());
        a.limit = 1000000.0; // not possible !!!!!
    }

}
```

Declare the limit-attribute final, will make it unchangeable after the initial value is set in the constructor.

Problem in this implementation: double number accuracy is not usable for finacial tasks. BigDecimal instead of double would be used in professional financial programms.


| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| check a basic class implementation, final modifier to prevent changes in values | completion task | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes, static modifier  

#### Learning Activities

1) read the Java code
2) understand the different methods
3) implement an instance of the class
4) run the code and review it for potential problems
5) implement and test a static modifier

#### Supporting information

Java-OOP-Poster: Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

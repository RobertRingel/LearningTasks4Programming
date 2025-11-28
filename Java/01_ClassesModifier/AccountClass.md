Topic: classes, modifiers

## Learning Task: Understand the Account class

The Java code below implements a basic bank account. Read the code to obtain an understandig. Describe the functionality provided by this class. Explain the pupose of the constructor. Why is checkAmount a private method?

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
This class models a basic bank account related to a named person. It is possible to book entries up to a certain limit and it is guaranteed that the balance will never be negative. The class has a method to get the current balance and to get name, account number and balance as a string.

The constructor is used to create account objects. Therefore a name and an account number must be given. The constructor sets the initial balance to zero and the transaction limit is set to 1000.0.

The checkAmount method is private, because it is a kind of class internal service method, a not a public service of the account class.


| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| classes encapsulate data, modifiers control access | worked-out example | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  

#### Learning Activities

1) read the Java code
2) understand the different attributes and methods
3) describe the functionality of the class
4) write brief answers to the questions

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 134-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

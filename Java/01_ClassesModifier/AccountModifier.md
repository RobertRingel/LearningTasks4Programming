Topic: classes, modifiers

## Learning Task: Extend the Account class

The Java code below implements a basic bank account. Add the following features to the code.  
- BIC (Bank Identifier Code) as a constant class attribute  
- change the number attribute to IBAN an make it unchangeable  

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

    public static final Sting BIC = "PBNKDEFF";

    private final String iban;
    private double balance;
    private double limit;
    private String name;

    public Account(String name, String iban) {
        this.iban = iban;
        this.balance = 0.0;
        this.limit = 1000.0;
        this.name = name;
    }

    ...

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : ");
        sb.append(Account.BIC);
        sb.append(" : ");
        sb.append(this.iban);
        sb.append(" : ");
        sb.append(this.balance);
        return sb.toString();
    }

}
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| choose modifiers, adapt code                   | completion task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes and modifieres  

#### Learning Activities

1) read the Java code
2) add the bic as static final attribute
3) change the number attribute to iban as a final attribute
4) perform code related changes to make it consistent

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

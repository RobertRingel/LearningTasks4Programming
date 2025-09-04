Topic: extension, interface

## Learning Task: The new Junior Account 

The code below shows two Java classes to model a specialized fixed deposit account as extension of a generic account. Read the code to obtain an understanding. 

Implement the new class JuniorAccout as extension of the Account-class. The junior account will be protected from getting a negative balance as result of any account action. Furthermore it account activities are limited to 1000 EUR. Develop the Java code of this class similar to the given sample code!  

The the new class with an appropriate main-method.

**The basic Account class:**
``` java
package org.htwd.pool.o2;

public class Account {
    private final String iban;
    private String person;
    private double balance;

    public Account(String iban, String person) {
        this.iban = iban;
        this.person = person;
        this.balance = 0.0;
    }

    public void account(double amount) {
        this.balance += amount;
    }

    public double getBalance() {
        return this.balance;
    }
}
```
*Note:* A professional financial program would use BigDecimal instead of double to implement the balance value. For the sake of focusing on the learning goals of this task we decided to use double here.

**The FixedDepositAccount class:**
``` java
package org.htwd.pool.o2;

public class FixedDepositAccount extends Account {

    private double savingsInterest = 0.035;

    public FixedDepositAccount(String iban, String person, double amount) {
        super(iban,person);
        if (amount > 0.0)
            super.account(amount);
    }

    public void account(double amount) {
        System.out.println("Service not available for FixedDepositAccount");
    }

    public double getValue() {
        return super.getBalance()*(1.0+this.savingsInterest);
    }

    public void setSavingsInterest(double rate) {
        this.savingsInterest = rate;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append(" : savings interest: ");
        sb.append(this.savingsInterest);
        sb.append(" : value EUR: ");
        sb.append(getValue());
        return sb.toString();
    }

}

```

---------------------------------------

### Solution
 
``` java
package org.htwd.pool.o2;

import static java.lang.Math.abs;

public class JuniorAccount extends Account {
    private final double limit = 1000.0;

    public JuniorAccount(String iban, String person) {
        super(iban, person);
    }

    public void account(double amount) {
        if (abs(amount) > this.limit || (this.getBalance()+amount)<0.0) {
            System.out.println("JuniorAccount limit violation!");
            return;
        }
        super.account(amount);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("JuniorAccount:");
        sb.append(super.toString());
        sb.append(" : limit EUR:");
        sb.append(this.limit);
        return sb.toString();
    }

    public static void main(String[] args) {
        JuniorAccount j = new JuniorAccount("DE3233319","Rico Reich");
        j.account(2000.0);
        j.account(300.0);
        j.account(-400.0);
        System.out.println(j);
    }
}
```


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply basic features of inheritance in Java      | imitation task  | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-1: basics of class extension 

#### Learning Activities

1) read the sample Java code
2) develop the new class, define the limit, overwrite the account method
3) test the implementation

#### Supporting information

Java-OOP-Poster: Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
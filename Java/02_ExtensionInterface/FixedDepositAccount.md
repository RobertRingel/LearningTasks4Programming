Topic: extension, interface

## Learning Task: Understand the FixedDepositAccount class

The Java code below implements two classes. Read the code to get an understanding. Implement a main-method to the FixedDepositAccount-class to demonstrate the usage of this class.

Write a brief description to the two classes to explain their purpose and the implementation.


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
 
Here is a sample implementation of the FixedDepositAccount.main-method: 


``` java
package org.htwd.pool.o2;

public class FixedDepositAccount extends Account {

...
    public static void main(String[] args) {
        FixedDepositAccount a = new FixedDepositAccount("DE221291", "Ricci Rich", 1000.0);
        a.account(-200.0);
        System.out.println(a);
    }

}
```

The Account-class is a very basic implementation of a bank account. It uses an IBAN number, a person string and a balance of data type double. It provides services to account to the balance and to get the current value of the balance. The toString-method provides the class internal data in string format.  
*Note:* A professional financial program would use BigDecimal instead of double to implement the balance value. For the sake of focusing on the learning goals of this task we decided to use double here.

The FixedDepositAccount class extends the Account class. Therefore it implements the additional attribute savingsInterest set to the initial value of 3.5%. The constructor calls the constructor of the Account class to set up the basic account. The statement 'super.account(amount);' initializes the amount of this account. Since the FixedDepositAccount models a fixed kind of saving account the account-method is re-implemented (overwritten) in a way that one can not use it for this class. The getValue-method is another overwritten method of the Account-class. It calculates the values of the savings account. To get the savings interes value one can call the appropriate get-method.  

Finally note the implementation of the toString-method in both of the classes. This method is always an overwritten method of the basic Java Object-class.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand basic features of inheritance in Java | worked-out example | 1 - low     |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
exi-1: basics of class extension and over-writing

#### Learning Activities

1) read the Java code
2) understand the different methods
3) briefly describe the functionality of the class
4) write a main-method to show the class usage

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 167-171

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

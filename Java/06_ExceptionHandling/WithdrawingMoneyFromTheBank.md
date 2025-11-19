Topic: exception handling

## Learning Task: Handling different exceptions

The BankAccount-class can be used to withdraw money from a bank account. The class itsself is working, however the main-method needs to be completed in a way to handle the exceptions.  
Implement the exception handling and explain the implementation in a few written sentences.

``` java
package org.htwd.pool.o6;

public class BankAccount {

    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public void withdraw(double amount) throws IllegalArgumentException, Exception {
        if (amount > balance)
            throw new Exception("Insufficient funds in the account");
        if (amount < 0.0)
            throw new IllegalArgumentException("Amount can not be negative");
        balance -= amount;
    }

    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);

        account.withdraw(-1500);
        System.out.println("Withdrawal successful. Remaining balance: " + account.getBalance());
    }
}
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

public class BankAccount {

...

    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        try {
            account.withdraw(-1500);
            System.out.println("Withdrawal successful. Remaining balance: " + account.getBalance());
        }
        catch(IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
``` 

The withdraw-method can throw an IllegalArgumentException in case one tries to withdraw a negative amount. Or it may throw a general Exception in case one will run into an insufficient funds situation.
The general Exception is the base class of all checked exceptions so it needs to be handled in a try-catch-block. The IllegalArgumentException is an unchecked exception, so there is no need to implement a try-catch-block for this exception.  
In case both exceptions shall be handled, the catch for the IllegalArgumentException must be implemented before the catch of the general Exception, otherwise the general Exception will also catch the IllegalArgumentException.

Consequently this implementation would also work:
``` java
package org.htwd.pool.o6;

public class BankAccount {

...

    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        try {
            account.withdraw(-1500);
            System.out.println("Withdrawal successful. Remaining balance: " + account.getBalance());
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
``` 


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling

#### Learning Activities

1) read the given Java code
2) implement the exception handling  
3) test the exception handling with help of the main-method implementation  
4) write a few statements to explain the implementation of the exception handling

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
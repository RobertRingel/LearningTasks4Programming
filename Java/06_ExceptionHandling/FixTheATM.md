Topic: exception handling

## Learning Task: The ATM needs a fix!

The following Java class is a demonstration of a very basic ATM terminal. It is based on the [ATMMachine class](ATMMachine.java). The run-method handles the user interaction with the terminal.  
As you will see, it is easily possible to let the program crash. Identify the weakness of the current implementation and fix-it with help of appropriate exception handling. 

``` java
package org.htwd.pool.o6;

import java.util.Scanner;

public class ATMMachineDemo {

    ATMMachine atm = new ATMMachine(0.0);

    public ATMMachineDemo() { }

    public void run() {
        String cmd ="";
        double amount = 0.0;
        Scanner sc = new Scanner(System.in);
        while (!cmd.equals("e")) {
            System.out.println("Balance, Deposit, Withdraw, End:");
            cmd = sc.nextLine();
            if (cmd.equals("b"))
                System.out.println(this.atm.checkBalance());
            if (cmd.equals("d") || cmd.equals("w")) {
                amount = sc.nextDouble();
                sc.nextLine();
                if (cmd.equals("d"))
                    this.atm.deposit(amount);
                if (cmd.equals("w"))
                    this.atm.withdraw(amount);
                System.out.println("New balance:" + this.atm.checkBalance());
            }
        }
        sc.close();
    }

    public static void main(String[] args) {
        ATMMachineDemo atmdemo = new ATMMachineDemo();
        atmdemo.run();
    }
}
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ATMMachineDemo {

    ATMMachine atm = new ATMMachine(0.0);

    public ATMMachineDemo() { }

    public void run() {
        String cmd ="";
        double amount = 0.0;
        boolean valid = false;
        Scanner sc = new Scanner(System.in);
        while (!cmd.equals("e")) {
            System.out.println("Balance, Deposit, Withdraw, End:");
            cmd = sc.nextLine();
            if (cmd.equals("b"))
                System.out.println(this.atm.checkBalance());
            if (cmd.equals("d") || cmd.equals("w")) {
                System.out.println("amount:");
                try {
                    amount = sc.nextDouble();
                    valid = true;
                } catch (InputMismatchException e) {
                    valid = false;
                    System.out.println(("invalid input."));
                }
                sc.nextLine();
                if (valid) {
                    if (cmd.equals("d"))
                        this.atm.deposit(amount);
                    if (cmd.equals("w"))
                        this.atm.withdraw(amount);
                    System.out.println("New balance:" + this.atm.checkBalance());
                }
            }

        }
        sc.close();
    }

...
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
uob-1: basics of creating and using objects  
exc-1: basics of exception-handling

#### Learning Activities

1) read and run the given Java code
2) identify potential code crash situation    
3) fix the code weakness to prevent crashes  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
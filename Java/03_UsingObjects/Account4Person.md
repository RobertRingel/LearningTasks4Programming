Topic: using objects

## Learning Task: Account for a Person 

The code below shows the two classes Person and Account. Read the given Java-code with focus on the constructor of the Account-class. Explain the difference between the two constructor variants of this class. What version of the Account-constructor is used in the main-method?

Add-on task: Name all the different classes used here in the code samples.

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
*Note:* For the sake of simplicity the birthday's date is modelled by a string instead of a date object.

---------------------------------------

### Solution
 
The Person-class models a person based on name and birthday. The Account-class models an account that is related to a person. Therefore the account has an IBAN, a balance and a Person-object as class attributes. The Account-constructor is implemented in two versions. One version takes a Person-object as input parameter to the constructor and stores it directly into the class attribute. The other version takes a person's name and birthday as input parameters in order to create a Person-object inside the constructor code. This object will be stored into the related class attribute.  

The given main-implementation uses the Account-constructor taking the Person-object as parameter. Therfore the Person-object is created in the line before the Account-object gets created.

List of all classes used in this sample code:  
Person, Account, String, StringBuilder


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand concepts of using objects             | worked-out example | 1 - low     |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  

#### Learning Activities

1) read the Java code
2) understand the different Account-constructor implementations
3) write a brief explanation of the constructor variants
4) identify and name all the different classes used in the given code

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

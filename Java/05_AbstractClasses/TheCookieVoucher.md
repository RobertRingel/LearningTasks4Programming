Topic: abstract classes

## Learning Task: The Cookie Voucher is real

Read the given Java code of the class AbstractVoucher. 
This class represents a basic and generic model of a voucher. Implement the class CookieVoucher as a sub-class of the AbstractVoucher.  
The CookieVoucher shall provide the reload-method to load the voucher for more cookies. Implement the main-method of the CookieVoucher-class to demonstrate its functionaliy.

``` java
package org.htwd.pool.o5;

public abstract class AbstractVoucher {

    static protected final double DEFAULT_VALUE = 100.0;

    private final String ID;

    protected double currentValue;

    public AbstractVoucher(String id) {
        this.currentValue = Voucher.DEFAULT_VALUE;
        this.ID = id;
    }

    abstract public boolean consume(double amount);

    public String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }
}
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o5;

public class CookieVoucher extends AbstractVoucher {

    public CookieVoucher(String name) {
        super(name);
    }

    @Override
    public boolean consume(double pieces) {
        if (pieces >= super.currentValue)
            return false;
        super.currentValue -= pieces;
        return true;
    }

    public boolean reload(double pieces) {
        if (pieces < 0.0)
            return false;
        super.currentValue += pieces;
        return true;
    }

    public static void main(String[] args) {
        CookieVoucher cv = new CookieVoucher("Liv");
        cv.consume(3.0);
        cv.reload(5.0);
        System.out.println(cv);
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the idea of abstract classes            | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) implement the new class CookieVoucher   
3) implement a main-Method to demonstrate the CookieVoucher  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
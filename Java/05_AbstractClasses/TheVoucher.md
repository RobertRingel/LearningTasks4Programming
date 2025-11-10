Topic: abstract classes

## Learning Task: The Voucher becomes abstract

Read the given Java code of the class Voucher. 
This class represents a basic and generic model of a voucher. But the implementation of the consume method should be realized in the specific sub-classes. This shall be done with help of an abstract class.  
Re-implement the Voucher-class as a new AbstractVoucher-class.

``` java
package org.htwd.pool.o5;

public class Voucher {

    static protected final double DEFAULT_VALUE = 100.0;
    
    private final String ID;
    
    protected double currentValue;

    public Voucher(String id) {
        this.currentValue = Voucher.DEFAULT_VALUE;
        this.ID = id;
    }

    public boolean consume(double amount) {
        if ((amount < 0.0) || ((this.currentValue-amount) < 0.0))
            return false;
        this.currentValue = this.currentValue - amount;
        return true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }

    public static void main(String args[]) {
        Voucher v = new Voucher("abc123");
        v.consume(10.0);
        System.out.println(v);
        v.consume(310.0);
        System.out.println(v);
    }
}
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o5;

public abstract class AbstractVoucher {

    static protected final double DEFAULT_VALUE = 100.0;

    private final String ID;

    private double currentValue;

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

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the idea of abstract classes            | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) implement the new class AbstractVoucher   

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

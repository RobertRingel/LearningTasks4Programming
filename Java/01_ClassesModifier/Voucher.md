Topic: classes, modifiers

## Learning Task: The Voucher needs modifiers

The code below represents the basic implementation of a voucher class. However the code is incomplete. All modifiers are missing. Add all modifiers to complete the Java code to make it runnable. Argument your decision for the choosen modifiers by comments in the code.

``` java
package org.htwd.pool.o1;

public class Voucher {
    double DEFAULT_VALUE = 100.0;
    String ID;
    currentValue;

    Voucher(String id) {
        this.currentValue = Voucher.DEFAULT_VALUE;
        this.ID = id;
    }

    boolean consume(double amount) {
        if ((amount < 0.0) || ((this.currentValue-amount) < 0.0))
            return false;
        this.currentValue = this.currentValue - amount;
        return true;
    }

    String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }

    void main(String args[]) {
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
package org.htwd.pool.o1;

public class Voucher {
    // a constant class variable visible inside the package
    static protected final double DEFAULT_VALUE = 100.0;
    
    // class internal and unchangable
    private final String ID;
    
    // class internal but changable
    private double currentValue;

    // Constructor is alsways public
    public Voucher(String id) {
        this.currentValue = Voucher.DEFAULT_VALUE;
        this.ID = id;
    }

    // the key functionality of the voucher -> public
    public boolean consume(double amount) {
        if ((amount < 0.0) || ((this.currentValue-amount) < 0.0))
            return false;
        this.currentValue = this.currentValue - amount;
        return true;
    }

    // a public service
    public String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }

    // public class method to start the program
    public static void main(String args[]) {
        Voucher v = new Voucher("abc123");
        v.consume(10.0);
        System.out.println(v);
        v.consume(310.0);
        System.out.println(v);
    }
}
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| choose the appropriate modifiers               | completion task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) read the Java code
2) decide for the appropriate modifiers
3) write short comments to argument the decision
4) run the code and test it

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

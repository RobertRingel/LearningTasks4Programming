Topic: extension, interface

## Learning Task: The new cinema voucher 

The code below shows two Java classes to model a specialized cinema voucher as extension of a generic voucher. Read the code to obtain an understanding. Add two more methods to the CinemaVoucher-class: 
- implement the toString-method with help of the Voucher.toString-method.  
- implement a method "reload20" to load 20 EUR to the CinemaVoucher.

Finally, write a list of all public method names of the CinemaVoucher-class!

**The basic Voucher class:**
``` java
package org.htwd.pool.o2;

public class Voucher {
    private final String name;
    private double value;

    public Voucher(String name) {
        this.name = name;
        this.value = 50.0;
    }

    public boolean consume(double amount) {
        if (this.value >= amount && amount > 0) {
            this.value -= amount;
            return true;
        }
        return false;
    }

    public boolean addMoney(double amount) {
        if (amount > 0) {
            this.value += amount;
            return true;
        }
        return false;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : value EUR:");
        sb.append(this.value);
        return sb.toString();
    }
}
```

**The CinemaVoucher class:**
``` java
package org.htwd.pool.o2;

public class CinemaVoucher extends Voucher {
    public static final double SPECIAL_PRICE = 7.0;
    public static final double STD_PRICE = 9.0;

    public CinemaVoucher(String name) {
        super(name);
    }

    public boolean buySpecialTicket() {
        return this.consume(CinemaVoucher.SPECIAL_PRICE);
    }

    public boolean buyStandardTicket() {
        return this.consume(CinemaVoucher.STD_PRICE);
    }

}
```

---------------------------------------

### Solution
 
Here is a sample implementation of the requested methods: 

``` java
package org.htwd.pool.o2;

public class CinemaVoucher extends Voucher {

    ...

    public void reload20() { 
        this.addMoney(20.0);
    }

    public String toString() { 
        StringBuilder sb = new StringBuilder("CinemaVoucher: ");
        sb.append(super.toString());
        return sb.toString();
    }

}
```

List of CinemaVoucher public methods:
- Constructor: CinemaVoucher
- toString
- addMoney
- reload20
- buySpecialTicket
- buyStandardTicket
- consume


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand basic features of inheritance in Java | completion task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
exi-1: basics of class extension 

#### Learning Activities

1) read the Java code
2) understand the different methods
3) implement the two requested methods
4) test the implementation
5) write the list of public class methods of CinemaVoucher

#### Supporting information

Java-OOP-Poster: Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

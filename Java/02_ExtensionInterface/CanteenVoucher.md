Topic: extension, interface

## Learning Task: The Canteen Voucher

The code below shows three Java classes. Read the code, run the program.  
Write a brief description of the classes with focus on the interface-methods.

**The interface class Consumable:**
``` java
package org.htwd.pool.o2;

public interface Consumable {
    public boolean consume(double amount);
    public double consumeAll();
}
```

**The interface class Reloadable:**
``` java
package org.htwd.pool.o2;

public interface Reloadable {
    public double reload(double amount);
    public double reloadTo(double value);
}
```

**The CanteenVoucher class:**
``` java
package org.htwd.pool.o2;

public class CanteenVoucher implements Reloadable, Consumable {

    private double value;
    private String name;

    public CanteenVoucher(String name) {
        this.name = name;
        this.value = 0.0;
    }

    public double reload(double amount) {
        if (amount < 0)
            return 0.0;
        this.value += amount;
        return amount;
    }

    public double reloadTo(double value) {
        if (value < this.value)
            return 0.0;
        double amount = value - this.value;
        this.value = value;
        return amount;
    }

    public boolean consume(double amount) {
        if (this.value >= amount && amount > 0) {
            this.value -= amount;
            return true;
        }
        return false;
    }

    public double consumeAll() {
        double v = this.value;
        this.value = 0.0;
        return v;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : value EUR:");
        sb.append(this.value);
        return sb.toString();
    }

    public static void main(String args[]) {
        CanteenVoucher c = new CanteenVoucher("Bob");
        c.reload(20.0);
        c.consume(5.00);
        double v = c.reloadTo(25.0);
        System.out.println(v);
        System.out.println(c);
        v = c.consumeAll();
        System.out.println(v);
    }
}
```

---------------------------------------

### Solution

The classes Reloadable and Consumable are interfaces used to define methods to be implemented by classes.   

The Reloadable-class defines two methods to reload money to a voucher. The reload-method puts the given amount of money to the voucher and returns the amount that was loaded. The reloadTo-method reloads a voucher up to the given value. It returns the amount of money that was loaded. Looking at the implementation of theses methods in the CanteenVoucher-class, one can see, that both methods will return 0.0 in case the loading could not be performed due to an invalid value of the method parameter.  

The Consumable-class defines two methods to perform consuming operations. The consume-method cosumes the given amount and returns true in case of success. The consumeAll-method consumes all money according to the current value of the voucher and it returns the value the was consumed. The remaining value at the voucher is zero.  

The 3rd class named CanteenVoucher implements both interfaces to model a voucher. Beside the implementation of the interface methods it has the private attributes name and value and a public toString-method. So it might be used to model a voucher. The main-method demonstrates the use of this class.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the interface definition and implementation | worked-out example | 1 - low |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-2: basics of interface definition and implementation 

#### Learning Activities

1) read the given Java code
2) run the given code
3) write a brief description of the consume-methods 

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 4

[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
Topic: extension, interface

## Learning Task: Vouchers are consumable

The code below shows two Java classes. Read the code, run the program.  
Write a brief description of the classes with focus on the consume-methods.

**The interface class Consumable:**
``` java
package org.htwd.pool.o2;

public interface Consumable {
    public boolean consume(double amount);
    public double consumeAll();
}
```

**The ConsumableVoucher class:**
``` java
package org.htwd.pool.o2;

public class ConsumableVoucher implements Consumable{
    private final String name;
    private double value;

    public ConsumableVoucher(String name) {
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

    public double consumeAll() {
        double c = this.value;
        this.value = 0.0;
        return c;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : value EUR:");
        sb.append(this.value);
        return sb.toString();
    }

    public static void main(String[] args) {
        ConsumableVoucher v = new ConsumableVoucher("Liv");
        boolean res = v.consume(5.0);
        System.out.println(res);
        res = v.consume(-5.0);
        System.out.println(res);
        System.out.println(v);
        v.consumeAll();
        System.out.println(v);
    }
}
```

---------------------------------------

### Solution

The Consumable-interface-class defines two consume-methods. The ConsumableVoucher-class implements this interface. Therefore it provides code for these two methods. 
The consume-method tries to consume the named amount. In case the amount is negative or the voucher's value is insufficient the method will return false. Otherwise it will consume the named amount from the voucher's value returning true.
The consumeAll-method consumes the complete value of the voucher and returns the consumed value as double.  
The implemented main-method demonstrates these implemted functionalities.


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

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 174-176

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

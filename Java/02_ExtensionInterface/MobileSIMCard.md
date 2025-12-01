Topic: extension, interface

## Learning Task: The mobile SIM card

The code below shows the interface definition classes Consumable and Reloadable. Furthermore the BasicVoucher core code that shall implement these interfaces is given.  
The PrePaidSimCard class extends the BasicVoucher to model a mobile phone sim card.

Read the given Java codes, identify and understand the gaps in the code. The complete the code by filling the gaps. Finally run and test your implementation. 

Help: The interface implementation is available in the given code of task [CanteenVoucher](CanteenVoucher.md).

**The interface classes Consumable and Reloadable:**
``` java
package org.htwd.pool.o2;

public interface Consumable {
    public boolean consume(double amount);  // consume req. amount
    public double consumeAll();   // consume all the money on voucher
}
```

``` java
package org.htwd.pool.o2;

public interface Reloadable {
    public double reload(double amount);  // reload req. amount
    public double reloadTo(double value); // reload to req. value
}
```

**The BasicVoucher class:**
``` java
package org.htwd.pool.o2;

public class BasicVoucher implements Consumable, Reloadable {

    private String name;
    private double value;

    public BasicVoucher(String name, double value) {
        this.name = name;
        this.value = value;
    }

    public double getValue() {
        return this.value;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Name:");
        sb.append(this.name);
        sb.append(" : Value EUR:");
        sb.append(this.value);
        return sb.toString();
    }

    // ... add missing methods ...

}
```

``` java
package org.htwd.pool.o2;

public class PrePaidSimCard extends BasicVoucher {
    public static final double STD_CALL_PRICE = 0.19;
    private String mobileNo;

    public PrePaidSimCard(String name, double value, String mobileNo) {
        // ... implement it
    }

    public boolean makeStandardCall() {
        // ... implement using consume method
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Mobile No:");
        sb.append(this.mobileNo);
        sb.append(" : ");
        sb.append(super.toString());
        return sb.toString();
    }

    public static void main(String[] ars) {
        PrePaidSimCard sim = new PrePaidSimCard("Sue", 20.0, "++42 1234 5678");
        sim.makeStandardCall();
        sim.consume(2.00);
        System.out.println(sim);
    }
}

```
---------------------------------------

### Solution

**The BasicVoucher class:**
``` java
package org.htwd.pool.o2;

public class BasicVoucher implements Consumable, Reloadable {

    private String name;
    private double value;

    ...

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
}
```

**The PrePaidSimCard class:**
``` java
package org.htwd.pool.o2;

public class PrePaidSimCard extends BasicVoucher {
    public static final double STD_CALL_PRICE = 0.19;
    private String mobileNo;

    public PrePaidSimCard(String name, double value, String mobileNo) {
        super(name, value);
        this.mobileNo = mobileNo;
    }

    public boolean makeStandardCall() {
        if (this.consume(STD_CALL_PRICE)) {
            System.out.println("... calling somebody...");
            return true;
        }
        System.out.println("... not enough money - reload please...");
        return false;
    }

    ...
}

```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| using extension and interface in Java classes    | completion task | 2 - normal       |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-1: basics of class extension  
exi-2: basics of interface definition and implementation  

#### Learning Activities

1) read the given Java code
2) identify and understand the gap in the code
3) implement the missing methods regarding class extension and interfaces
4) run and test the complete code 

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Boxes 3, 4

[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 174-176

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

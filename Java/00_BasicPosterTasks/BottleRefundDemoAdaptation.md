Topic: Basic Java programming

## Learning Task: Adapting class functionality

The Java code below shows the original class implementation of BottleCase and RefundStation.  
Add a new method "emptyCase()" to the BottleCase class that will reset the class internal count variable to zero. Adapt the implementation of the returnCase-method in class RefundStation to call the emptyCase-method for a returned BottleCase to really empty it.

**Class BottleCase**
``` java
package org.htwd.refund;

public class BottleCase {
    private double BOTTLEVALUE = 0.08;
    private final int CAPACITY;
    private int count;

    public BottleCase(int capacity) {
        this.CAPACITY = capacity;
        this.count = 0;
    }

    public void addMore(int n) {
	 if (n > 0 && (this.count+n) <= this.CAPACITY) {
            this.count = this.count + n;
        }
    }

    public double getTotalValue() {
        return this.BOTTLEVALUE * this.count;
    }
}
```

**Class RefundStation**
``` java
package org.htwd.refund;

public class RefundStation {
    private int collectedCases;
    private double sumRefund;

    public RefundStation() {
        this.collectedCases = 0;
        this.sumRefund = 0.0;
    }

    public double returnCase(BottleCase c) {
        this.collectedCases++;
        double val = c.getTotalValue();
        this.sumRefund = this.sumRefund + val;
        return val;
    }

    public void printStatus() {
        System.out.println("collected Cases:   " 
				+ this.collectedCases);
        System.out.println("Sum of refund EUR: " 
					+ this.sumRefund);
    }
}
```
---------------------------------------

### Solution

**Class BottleCase**
``` java
package org.htwd.refund;

public class BottleCase {
    
    ...
    public void emptyCase() {
        count = 0; 
    }
    ...
}
```

**Class RefundStation**
``` java
package org.htwd.refund;

public class RefundStation {
 ...
     public double returnCase(BottleCase c) {
        collectedCases++;
        double val = c.getTotalValue();
        sumRefund = sumRefund + val;
        c.emptyCase();
        return val;
    }
 ...
}
```

**Note:** The line "c.emptyCase()" must be located after the line "double val = c.getTotalValue()".

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| adaptation of interacting classes                | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types  
- bcm-1: basics of classes, public/private modifieres  
- Box 6: Make use of objects shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) implement a new method in class BottleCase
2) adapt method in class RefundStation
3) run and test the adapted code

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 6 

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 116/117

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

Topic: Basic Java programming

## Learning Task: Make Use of Objects

The Java code in this task is a bit more complex. We are going to consider the interaction of the three classes shown below. Read the code and run the code. Finally write a few notes to describe the purpose of each class.  

*Note:* Do not forget: each java class must been implemented in separate a Java file.  

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

**Class BottleRefundDemo**
``` java
package org.htwd.refund;
import java.util.Random;

public class BottleRefundDemo {

    public static void main(String[] args) {
        Random rnd = new Random();
        int n = rnd.nextInt(10)+1;
        int number;
        int i = 0;

        BottleCase b = null;
        // create BottleCases in an array
        BottleCase[] cases = new BottleCase[n];
        while ( i < cases.length ) {
            b = new BottleCase(20);
            number = rnd.nextInt(15)+1;
            b.addMore(number);
            cases[i] = b;
            i++;
        }

        // process all the BottleCases 
	    // at the RefundStation
        RefundStation r = new RefundStation();
        r.printStatus();
        i = 0;
        BottleCase c = null;
        while ( i < cases.length ) {
            c = cases[i];
            r.returnCase(c);
            i++;
        }
        r.printStatus();
    }
}
```

---------------------------------------

### Solution

**Class BottleCase** models a case to carry collected bottles. The case has a limited capacity that is checked when adding more bottles to the case. The value of one bottle is set to 0.08 - that is the bases to calculate the refund value of the current content of the bottle case.

**Class RefundStation** models a machine to consume empty bottle cases for recycling. By returning a bottle case it evaluates the number of bottles in the case and returns the according refund value. Internally the machine cumulates the number of collected cases and the value of refund.

**Class BottleRefundDemo** implements just a main-method to demonstrate the usage of the classes BottleCase and RefundStation. The main-method uses a random number generator to create a random number of BottleCase objects that will get filled with a random amount of empty bottles. The RefundStation object is used to collect all the bottle cases and to print its status finally.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use and interaction of objects  | worked-out exampe | 2 - normal     |  

#### Previous Knowledge

- variables and data types,  
- Box 6: Make use of objects shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 116/117

#### Learning Activities

1) read the code
2) run the code to understand it
3) write brief notes to explain the classes

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 6 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

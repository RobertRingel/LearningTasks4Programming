Topic: Basic Java programming

## Learning Task: Adapting class functionality II

The Java code below shows the original class implementation of RefundStation.  
Add a new method "simulateError()" to the RefundStation class. Add an boolean attribute "active" to the class. The simulateError-method will cause a random error (probability 30%) to set active to false. Such an error will prevent to return any bottle case. Adapt the returnCase-method accordingly. Add a call to the simulateError-method at the 1st line of the returnCase-method. Finally run and test the new code - e.g. by running the BottleRefundDemo.

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

``` java
package org.htwd;
import java.util.Random;

public class RefundStation {
    private int collectedCases;
    private double sumRefund;
    private boolean active;

    public RefundStation() {
        collectedCases = 0;
        sumRefund = 0.0;
        active = true;
    }

    public void simulateError() {
        Random rnd = new Random();
        int n = rnd.nextInt(10);
        if (n<3) {
            active = false;
            System.out.println("Machine Error!");
        } else {
            active = true;
        }
    }

    public double returnCase(BottleCase c) {
        simulateError();
        if (active == false)
            return 0.0;
        collectedCases++;
        double val = c.getTotalValue();
        sumRefund = sumRefund + val;
        c.emptyCase();
        return val;
    }

    public void printStatus() {
        System.out.println("active:            " + active);
        System.out.println("collected Cases:   " + collectedCases);
        System.out.println("Sum of refund EUR: " + sumRefund);
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| adaptation of an existing classes                | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 6: Make use of objects shown in the Basic Java Poster (JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) implement the new attribue and the new method
2) adapt existing methods in the class accordingly
3) run and test the adapted code

#### Supporting information

Basic Java-Poster: Box 6 ... Weblink

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

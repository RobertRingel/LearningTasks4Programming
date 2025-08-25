Topic: Basic Java programming

## Learning Task: Understand the BottleCase class

The Java code below implements a bottle case to collect refund bottles. Read and run the code to obtain an understandig. Describe the functionality provided by this class. 

``` java
package org.htwd.pool.o0;

public class BottleCase {
    private final double BOTTLEVALUE = 0.08;
    private final int CAPACITY;
    private int count;

    public BottleCase(int capacity) {
        this.CAPACITY = capacity; 
        this.count = 0;
    }

    public void addMore(int n) {
        this.count = this.count + n;
    }

    public double getTotalValue() {
        double v = this.BOTTLEVALUE * this.count;
        return v;
    }

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        b.addMore(8);
        System.out.println("EUR: " + 
		      b.getTotalValue());
    }

}
```

---------------------------------------

### Solution
This class models a bottle case to collect bottles for refund. The case has a defined capacity that gets set by the constructor. The initial bottle count is set to zero by the constructor. The value of a bottle is defined to 0.08. The addMore method increments the count of collected bottles by n. The getTotalValue method calculates the value of bottles that have been added to the case. The provided main-function demonstrates the usage of this class.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| describe the functionality of a basic Java class | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types,  
- Box 1: Example of a Java class shown in the Basic Java Poster (JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) run the Java code
3) understand the class, its attributes, the constructor and the methods
4) describe the functionality of the class

#### Supporting information

Basic Java-Poster: Box 1 ... Weblink

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

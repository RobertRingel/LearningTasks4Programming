Topic: Basic Java programming

## Learning Task: Review the BottleCase class

The Java code below shows the implementation of the BottleCase class. The class models the collection of refund bottles. Read and review the code. Can you identify some weaknesses of the current implementation? Write some brief notes to name your findings.

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

    public int availableCapacity() {
        int c = this.CAPACITY - this.count;
        return c;
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

The consturctor parameter capacity should be checked for sanity before it will be assigned to the class attribute CAPACITY. Currently one could define a negative capacity without any problem.

The addMore-method should check the available capacity before the amount of n items will be added. Currently it is possible to overrun the capacity limit without any problem.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| read and critical review given code              | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types  
- Box 1: Example of a Java class shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  
- bcm-1: basics of classes, public/private modifieres

#### Learning Activities

1) read the Java code
2) identify critical situations and evaluate them (mentally perform the code) 
3) write notes to explain the identified problems  

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 1

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 135-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

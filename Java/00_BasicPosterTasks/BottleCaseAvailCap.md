Topic: Basic Java programming

## Learning Task: New method for class BottleCase

The Java code below shows the implementation of the BottleCase class. The class models the collection of refund bottles. Implement the new method availableCapacity to calculate the number of bottles that can be added until the defined capacity limit is reached. 

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

``` java
package org.htwd.pool.o0;

public class BottleCase {
    private final double BOTTLEVALUE = 0.08;
    private final int CAPACITY;
    private int count;

    ...

    public int availableCapacity() {
        int c = this.CAPACITY - this.count;
        return c;
    }
    
    ...

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        b.addMore(8);
        int c = b.availableCapacity();
        System.out.println("available Capacity: " + c);
        System.out.println("EUR: " + 
		      b.getTotalValue());
    }

}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| implement a new method into a basic Java class   | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types  
- Box 1: Example of a Java class shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)
- bcm-1: basics of classes, public/private modifieres

#### Learning Activities

1) read the Java code
2) implement the new method
3) test the new method in the main-code section  

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 1  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.:  
Chapter 5, pages 135-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

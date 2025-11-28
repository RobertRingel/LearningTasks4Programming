Topic: Basic Java programming

## Learning Task: Understand the BottleCase constructor

The Java code below shows the implementation of the BottleCase class. The class models the collection of refund bottles. Write a brief explanation of the constructor. 

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
A constructor is a special method of each Java class. It will be performed whenever a new object of a class gets created. It is used to initalize the object by assigning propper initial values to the class attributes. The shown implementation sets the variable count to zero (number of bottles in the bottle case). Furthermore the capacity limit of the bottle case object is set according to the given parameter.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| describe the function of a constructor           | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types,  
- Box 1: Example of a Java class shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) run the Java code
3) understand the constructor  
4) write a short description of the constructor  

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 1

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 155-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

Topic: Basic Java programming

## Learning Task: Implement Capacity Check

The Java code below shows the limited capacity of the bottle case. The addMore-method is used to add a certain amount of bottles to the case. However the given implementation of this method does not prevent to overrun the capacity limit. Improve the implementation of addMore in a way the capacity limit will not be exceeded! Write a main-method to test your implementation.

``` java
package org.htwd.pool.o0;

public class BottleCase {

    private final int CAPACITY;
...

    public BottleCase(int capacity) {
        if (capacity > 0) {
            this.CAPACITY = capacity;
        } else {
            this.CAPACITY = 0;
            System.out.println("Capacity set to 0");
        } 
        this.count = 0;
    }

    public void addMore(int n) {
        if (n < 0) {
            System.out.println("You try to remove bottles!!!");
            return;     // terminate method at this line with no return value
        }
        this.count = this.count + n;
    }

}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public void addMore(int n) {
        if (n < 0) {
            System.out.println("You try to remove bottles!!!");
            return;     // terminate method at this line with no return value
        }
	    if (n > 0 && (this.count+n) <= this.CAPACITY) {
            this.count = this.count + n;
        }
        else {
            System.out.println("Capacity limit - you would overload the case.");
        }
    }

}
``` 

Another implemention is also possible:

``` java
package org.htwd.pool.o0;

public class BottleCase {

... 

    public void addMore(int n) {
        if (n < 0) {
            System.out.println("You try to remove bottles!!!");
            return;     // terminate method at this line with no return value
        }
	    if (n > 0 && (this.count+n) <= this.CAPACITY) {
            this.count = this.count + n;
            return;    // terminate method at this line with no return value
        }
        this.count = this.CAPACITY;
        System.out.println("Due to capacity limit not all bottles were added.");
    }

    // test the addMore implementation
    public static void main(String[] args) {
        BottleCase b = new BottleCase(10);
        b.addMore(8);
        b.addMore(4);
        System.out.println("bottle count:"+b.count);
    }

}
``` 


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| make use of if-else-statements                   | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types  
- Box 3: Conditional execution shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)
- bcm-1: basics of classes, public/private modifieres  

#### Learning Activities

1) read the Java code and understand the problem
2) implement a solution for the problem
3) test the implementation by writing an appropriate main-method

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 3 

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 104/105

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

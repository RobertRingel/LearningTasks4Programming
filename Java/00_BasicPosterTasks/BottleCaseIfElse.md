Topic: Basic Java programming

## Learning Task: Understand conditional execution

The Java code below demonstrates the use of if-else-statements to improve some method implementation in the BottleCase class. Read the code, run it and write some brief notes to explain the new functionality of it.

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public BottleCase(int capacity) {
        if (capacity > 0) {
            this.CAPACITY = capacity;
        } else {
            this.CAPACITY = 0;
            System.out.println("Capa. set to 0");
        } 
        this.count = 0;
    }

    public void addMore(int n) {
        if (n > 0) {
            this.count = this.count + n;
        }
    }

}
```

---------------------------------------

### Solution

The new implementation of the constructor checks the value of the capacity parameter. In case it is reasonable (not negative) it will be accepted and assigned to the class attribute. Otherwise the attribute will be set to zero and a message will be shown.

The new addMore method will really add bottles to the bottle case. Because only positive values of n will be added to the count attribute. Negative values of variable n will not have any effect.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of if-else-statements         | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types,  
- Box 3: Conditional execution shown in the Basic Java Poster (JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) run it to gain understandig 
3) write a brief explanation of the code functionality

#### Supporting information

Basic Java-Poster: Box 3 ... Weblink

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

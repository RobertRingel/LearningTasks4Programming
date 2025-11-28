Topic: Basic Java programming

## Learning Task: Really adding bottles 

The Java code below shows the implementation of the addMore-method to add more bottles to the case. Add a warning message to the implementation that will inform the user in case nothing was added because n was not greater than zero.

Test the implementation using with help of the given main-method.

``` java
package org.htwd.pool.o0;

public class BottleCase {

	...

    public void addMore(int n) {
        if (n > 0) {
            this.count = this.count + n;
        }
    }

    ...

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        b.addMore(0);
        b.addMore(-2);
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
        if (n > 0) {
            this.count = this.count + n;
        }
        else {
            System.out.println("n: " + n + " nothing added to the case");
        }
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| make use of the else-statement                   | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 3: Conditional execution shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) understand the problem
2) implement an else-statement
3) run the code to test the implementation 

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 3 

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 104/105

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

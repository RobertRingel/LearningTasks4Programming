Topic: Basic Java programming

## Learning Task: Identifying Objects

The Java code below uses objects of different classes. Read the code and highligt all lines the make use of these objects.

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

``` java
package org.htwd.refund;
import java.util.Random;

public class BottleRefundDemo {

    public static void main(String[] args) {
        Random rnd = new Random();              // create Random object
        int n = rnd.nextInt(10)+1;              // use Random
        int number;
        int i = 0;

        BottleCase b = null;                    // declare object variable
        // create BottleCases in an array
        BottleCase[] cases = new BottleCase[n]; // create array of objects
        while ( i < cases.length ) {            
            b = new BottleCase(20);             // create BottleCase
            number = rnd.nextInt(15)+1;         // use Random
            b.addMore(number);                  // use BottleCase
            cases[i] = b;                       // store BottleCase
            i++;
        }

        // process all the BottleCases 
	    // at the RefundStation
        RefundStation r = new RefundStation();  // create RefundStation
        r.printStatus();                        // use RefundStation
        i = 0;
        BottleCase c = null;                    // declare object variable
        while ( i < cases.length ) {
            c = cases[i];                       // read BottleCase
            r.returnCase(c);                    // use RefundStation and BottleCase
            i++;
        }
        r.printStatus();                        // use RefundStation
    }
}
```


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use and interaction of objects | worked-out example | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 6: Make use of objects shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the code
2) mark all uses of objects

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 6 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

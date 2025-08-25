Topic: Basic Java programming

## Learning Task: Breaking the loop

The Java code below shows the main-function of class BottleCase. It has the example of a while-true-loop and it demonstrates the effect of the break-statement to exit this loop. 
Read the code, run it and write some brief note to explain the function of this particular implementation of the while-loop.

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        int num = 0;

        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Number of bottles to add? (Stop: <=0)"); 
            num = sc.nextInt();
            sc.nextLine();
            if (num <= 0) {
                break;
            }
            b.addMore(num);
        }

        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        sc.close();
    }
}
```

---------------------------------------

### Solution

The while(true)-statement implements a loop to run potentially endless. Such a kind of loop needs to have a break-statement that will be performed under a certain condition to exit the loop. In the given code the while-loop be terminated in case the user enters a value of less than one as the number of bottles. In this case the lines  
<pre>
    if (num <= 0) {  
        break;  
    }  
</pre>
will perform the break-statement to exit the loop.

**Note:** a break-statement will exit a loop in any case, not just for a while(true)-loop.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of a break statement          | worked-out example | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 4: Loops shown in the Basic Java Poster (JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the given main-method
2) run the program
3) write a brief note to explain the given loop-implementation

#### Supporting information

Basic Java-Poster: Box 4 ... Weblink

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

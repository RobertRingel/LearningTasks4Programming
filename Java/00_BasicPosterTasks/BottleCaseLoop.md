Topic: Basic Java programming

## Learning Task: Adding more and more bottles 

The Java code below shows the main-function of class BottleCase in order to demonstrate the implementation of a while-loop. Read the given code, run it and write some brief note to explain the function and the purpose of the while-loop.

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        int num = 0;

        Scanner sc = new Scanner(System.in);
        System.out.println("How many people 	
			          collected bottles?");
        int people = sc.nextInt();
        sc.nextLine();
        
        while (people > 0) {
            System.out.println("Number of bottles to add?"); 
            num = sc.nextInt();
            sc.nextLine();
            b.addMore(num);
            people = people - 1;
        }

        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        sc.close();
    }
}
```

---------------------------------------

### Solution

The while loop is used to repeat a section of code. The given while loop allows to enter and add the number of bottles for a dedicated number of people. 
So as long as the number of people is greater zero, it will read the number of bottles as an integer from the console and it will perform the addMore-method. Very important: at the end of the loop the number of people is decremented by one - otherwise the loop would run endless.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the implementation of a while-loop | worked-out example | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 4: Loops shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the given main-method
2) run the program
3) write a brief explanation of the while-loop 

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 4

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 108/109

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

Topic: Basic Java programming

## Learning Task: There is a problem with loop

The Java code below shows the main-function of class BottleCase in order to demonstrate the implementation of a while-loop. However the given implementation has a problem. Read the given code, run it, identify and fix the problem.

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
            people = people + 1;
        }

        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        sc.close();
    }
}
```

---------------------------------------

### Solution

Since the line "people = people + 1" will increment the number of people the while-statement "while (people>0)" will never stop the loop. The line must be corrected to:  
people = people - 1

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the implementation of a while-loop | worked-out example | 1 - low        | 

#### Previous Knowledge

- variables and data types,  
- Box 4: Loops shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the given main-method
2) run the program and identify the problem
3) fix the problem and test it

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 4 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

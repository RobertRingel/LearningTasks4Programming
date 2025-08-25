Topic: Basic Java programming

## Learning Task: Write some console inputs

The Java code below demonstrates Java code for console input. Change the implementation of the main-method in a way the user will enter the number of bottles to add three times one after the other. Change the code accordingly, run it and test it. A straightforward implementation without loop is ok for this exercise.

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public static void main(String[] args) {
        BottleCase b = new BottleCase(20);
        b.addMore(3);
        System.out.println("Bottles to add?");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.nextLine();
        
        b.addMore(num);
        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        System.out.println("What's your name?");
        String name = sc.nextLine();
        System.out.println("Great job " + name);
        sc.close();
    }

}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o0;

public class BottleCase {

...

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BottleCase b = new BottleCase(20);

        System.out.println("Bottles to add?");
        int num = sc.nextInt();
        sc.nextLine();
        b.addMore(num);
        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        System.out.println("Bottles to add?");
        num = sc.nextInt();
        sc.nextLine();
        b.addMore(num);
        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        System.out.println("Bottles to add?");
        num = sc.nextInt();
        sc.nextLine();
        b.addMore(num);
        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        System.out.println("What's your name?");
        String name = sc.nextLine();
        System.out.println("Great job " + name);

        sc.close();
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| code an integer console input                    | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 2: Console input shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) add code lines to read the bottle count from console
3) run the Java code

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 2

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

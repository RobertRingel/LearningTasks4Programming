Topic: Basic Java programming

## Learning Task: User-defined capacity limit

The Java code below creates a BottleCase object of a capacity of 20 bottles. This number 20 is hard-coded in the main-function of the Java class. Change the code in a way that the capacity will be entered by the user as the program is running.

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
        System.out.println("Enter bottle case capacity!");  
        Scanner sc = new Scanner(System.in);
        int cap = sc.nextInt();
        sc.nextLine();

        BottleCase b = new BottleCase(cap);
        System.out.println("CAPACITY:"+b.CAPACITY);
        
        b.addMore(3);
        System.out.println("Bottles to add?");  

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

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| code an integer console input                    | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types  
- Box 2: Console input shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)
- bcm-1: basics of classes, public/private modifieres

#### Learning Activities

1) read the Java code
2) add code lines to read the capacity value from console
3) run the Java code
4) optional add an extra line to display the capacity that has been set

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 2 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

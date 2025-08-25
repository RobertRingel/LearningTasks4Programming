Topic: Basic Java programming

## Learning Task: Understand console input

The Java code below demonstrates the basic implementation of console input. It shows how to read numbers and text entered by the user of the program. Read the code, run it and write some notes into code to explain it.

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
        BottleCase b = new BottleCase(20);
        b.addMore(3);
        // console output shown on the screen
        System.out.println("Bottles to add?");  
        // create a scanner object to read from keyboard
        Scanner sc = new Scanner(System.in);
        // read an integer number to a variable
        int num = sc.nextInt();
        // read all remaining characters until EOL
        sc.nextLine();
        
        b.addMore(num);
        System.out.println("We have total EUR: " 
            + b.getTotalValue());

        System.out.println("What's your name?");
        // read all characters including EOL into string variable
        String name = sc.nextLine();            
        System.out.println("Great job " + name);
        // close the scanner object
        sc.close();
    }

}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand console input                         | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types,  
- Box 2: Console input shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) run the Java code
2) understand the usage of the scanner-object
3) write comments to explain the scanner functionality in the given code

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 2 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

Topic: Basic Java programming

## Learning Task: Use arrays to store data

The Java code below demonstrates the use of an array. Read the code and run it.
Highlight all lines that are related to array-functionality. Write some brief notes to explain it. 

``` java
public static void main(String[] args) {
    int count;
    Scanner sc = new Scanner(System.in);

    BottleCase b;
    BottleCase[] cases = new BottleCase[3];

    int i = 0;
    while (i < cases.length) {
        b = new BottleCase(20);
        System.out.println("How many bottles to add?"); 
        count = sc.nextInt();
        sc.nextLine();
        b.addMore(count);
        cases[i] = b;
        i = i + 1;
    }
    sc.close();
        
    double sum = 0.0;
    i = 0;
    while (i < cases.length) {
        b = cases[i];
        sum = sum + b.getTotalValue();
        i = i + 1;
    }
        
    System.out.println("We have total EUR: " + sum);
}
```

---------------------------------------

### Solution

``` java
public static void main(String[] args) {
    int count;
    Scanner sc = new Scanner(System.in);

    BottleCase b;
    BottleCase[] cases = new BottleCase[3];    // <<<< Array

    int i = 0;                                 // <<<< Array
    while (i < cases.length) {                 // <<<< Array
        b = new BottleCase(20);
        System.out.println("How many bottles to add?"); 
        count = sc.nextInt();
        sc.nextLine();
        b.addMore(count);
        cases[i] = b;                          // <<<< Array
        i = i + 1;                             // <<<< Array
    }
    sc.close();
        
    double sum = 0.0;
    i = 0;                                     // <<<< Array
    while (i < cases.length) {                 // <<<< Array
        b = cases[i];                          // <<<< Array
        sum = sum + b.getTotalValue();
        i = i + 1;                             // <<<< Array
    }
        
    System.out.println("We have total EUR: " + sum);
}
```

The main-method-example creates an array-variable cases to store 3 BottleCase-objects. Within the first while-loop the 3 BottleCase objects are created and filled with a number of bottles according to the users input. The BottleCase-objects are assigned to an array index position to get stored. Therefore the integer index variable i is used to to access the array elements 0, 1, 2.  
The second while-lopp is implemented similarly to iterate the array-variable cases once more. This time all the array entries are read in order to sum up their values.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of arrays                     | worked-out example | 2 - normal  |  

#### Previous Knowledge

- variables and data types,
- loops,
- console input,
- bcm-1: basics of classes, public/private modifieres,  
- Box 5: Arrays to store data shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) read the Java code
2) run it to gain understandig 
3) highlight all code lines related to array operations
4) write a brief explanation of the code functionality with focus on the array

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 5

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 120-130

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

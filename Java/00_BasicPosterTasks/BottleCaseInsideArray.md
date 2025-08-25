Topic: Basic Java programming

## Learning Task: Dig into the array

The Java code below demonstrates the use of an array. Lets have a look into the array represented by the variable cases. Navigate to the code section of the second while-loop and add a Java-statement to print the value of the variable i and the content of the array entry at index position i.  

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
    
    ...

    double sum = 0.0;
    i = 0;                                     
    while (i < cases.length) {                 
        // the following line shall be implemented
        System.out.println("i: " + i + " cases[i]: " + cases[i]); 
        b = cases[i];                          
        sum = sum + b.getTotalValue();
        i = i + 1;                             
    }
        
    System.out.println("We have total EUR: " + sum);
}
```
The print-statements will cause an output similar to this:  
i: 0 cases[i]: org.htwd.pool.o0.BottleCase@23fc625e  
i: 1 cases[i]: org.htwd.pool.o0.BottleCase@3f99bd52  
i: 2 cases[i]: org.htwd.pool.o0.BottleCase@4f023edb  

Note the values of i running from 0 to 2 as the first index of an Java-array is always zero.
The values of cases[i] are the Java-internal references to the BottleCase-class objectes.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of arrays                     | worked-out example | 1 - low     |  

#### Previous Knowledge

- variables and data types,  
- Box 5: Conditional execution shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) implement the line for the requested print-output
2) run the program
3) watch and understand the print-out

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 5 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

Topic: Basic Java programming

## Learning Task: Lots of Bottle Cases

The Java code below demonstrates the use of an array. Change to code in a way, the user will enter the desired number of BottleCases.  

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

    // --- new code section of 3 lines ---
    System.out.println("How many bottles cases do you want?"); 
    int numCases = sc.nextInt();
    sc.nextLine();
    
    BottleCase b;
    BottleCase[] cases = new BottleCase[numCases]; // <<< important change here

    ...

    System.out.println("We have total EUR: " + sum);
}
```

The user must be able to enter the desired number of bottle cases before the array cases get created. This is implemented in the "new code section". The number gets assigned to the int-variable numCases. This variable numCases must replace the number 3 at the array declaration "BottleCase[] cases = new BottleCase[3];"

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the declaration of arrays             | completion task | 1 - low        |  

#### Previous Knowledge

- variables and data types,  
- Box 5: Arrays to store data shown in the [Basic Java Poster](00_JavaPoster_HK_engl.pdf)  

#### Learning Activities

1) identify the code section to be changed
2) implement the code adaptation
3) run and test the adapted program

#### Supporting information

[Basic Java Poster](00_JavaPoster_HK_engl.pdf): Box 5

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 4, pages 120-130

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

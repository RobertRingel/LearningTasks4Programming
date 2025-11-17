Topic: exception handling

## Learning Task: Valid person data

Read the given Java code of the Person-class with focus on the constructor. Test and run the code.
Write a brief description of the constructor and the use of the constructor shown in the main-method of class.

``` java
package org.htwd.pool.o6;

import java.util.regex.Pattern;

public class Person {
    private String name;
    private final String birthDay;

    public Person(String name, String bday) throws IllegalArgumentException {
        if (name == null || name=="")
            throw new IllegalArgumentException("Invalid parameter for name");
        // Pattern.matches: perform basic date format check: DD/MM/YYYY
        if (bday == null || Pattern.matches("^\\d{2}[/-]\\d{2}[/-][012]\\d{3}$", bday) == false)
            throw new IllegalArgumentException("Invalid parameter for bday");
        this.name = name;
        this.birthDay = bday;
    }

    public String getName() { return this.name; }
    public String getBirthDay() { return this.birthDay; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append(" : ");
        sb.append(this.getBirthDay());
        return sb.toString();
    }

    public static void main(String[] args) {
        try {
            Person max = new Person("Max", "07.11/2002");
            System.out.println(max);
        } catch (IllegalArgumentException e) {
            System.out.println("There is a problem: "+e.getMessage());
        }
        System.out.println("regular end of the program");
    }
}
``` 

---------------------------------------

### Solution

The implementation of the Person-constructor performs checks to ensure valid data for the parameters name and bday. In case of invalid parameters an IllegalArgumentException will be created and thrown by the constructor. Throwing the exception terminates the constructor immedately, preventing a Person-object to be created. In case the data is found to be valid, the parameters will be stored as class attributes and the new Person-object will be created.  

The main-method encapsulates the constructor call within a try-catch-block that is able to catch IllegalArgumentExceptions. In case of an exception an error message will be shown. The print-out will show the particular exception message. And the program will not crash.  

In any case the program will end in a regular way.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the idea of exception handling        | worked-out example | 1 - low     | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling

#### Learning Activities

1) read the given Java code
2) manipulate and run the code for different data values  
3) write a brief description explaining the concepts of the exception implementation   

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
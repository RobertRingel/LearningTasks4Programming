Topic: exception handling

## Learning Task: A parser for German aircraft codes

The given Java program represents a custom exception class that shall be thrown in case parsing aircraft codes fails. 
The German aircraft codes can be described by the followin regular expression: D-[A-Z]{4}  
So they always start with "D-" followed by 4 capital letters.  

Implement a Java class that works as a parser for German aircraft codes. The class shall provide a static parse method that will throw an AircraftCodeParseException in case of a non matching aircraft code.  
Test your implementation with help of a main-method implementation.

``` java
package org.htwd.pool.o6;

public class AircraftCodeParseException extends RuntimeException {

    public AircraftCodeParseException(String s) {
        super(s);
    }
}
``` 

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

import java.util.regex.Pattern;

public class AircraftCodeParser {
    public static void parse(String code) throws AircraftCodeParseException {
        // regEx for valid German aircraft code: D-[A-Z]{4}
        if (Pattern.matches("^D-[A-Z]{4}$", code) == false)
            throw new AircraftCodeParseException(code+" is not a valid German aircraft code");
    }

    public static void main(String[] args) {
        AircraftCodeParser.parse("D-ACNX");
        AircraftCodeParser.parse("T-ACN11");
    }
}
``` 


| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply exception handling in problem solving      | conventional task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling  
basic regualar expression pattern matching as shown in task [TightenYourClass](TightenYourClass.md)  

#### Learning Activities

1) read the given Java exception class 
2) implement the requested parser class  
3) test the parser class using an appropriate main-method    

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  
basic regualar expression pattern matching as shown in task [TightenYourClass](TightenYourClass.md)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
Topic: classes, modifiers

## Learning Task: Printing tickets

The Java code below implements a ticket generator. Read the code to obtain understandig. Describe the functionality provided by this class and argument the different types of attribute modifiers.

Write a main-method to demonstrate the use of this class.

``` java
package org.htwd.pool.o1;

public class TicketGenerator {
    private static final String COMPANY = "iTicket Sales International Inc.";
    private final String ticketLabel;
    private int ticketCounter = 0;
    

    public TicketGenerator(String label) {
        this.ticketLabel = label;
    }

    public String getTicket() {
        this.ticketCounter++;
        String ticket = this.ticketLabel + ":" + this.ticketCounter;
        ticket = ticket + "\n" + TicketGenerator.COMPANY;
        return ticket;
    }

    public int getTicketCounter() {
        return this.ticketCounter;
    }
}
```

---------------------------------------

### Solution

The TicketGenerator is used to simulate the generation of unique strings that may serve as event tickets. The class constructor takes a string that names the event the tickets are made for. The class has an internal counter to count the number of generated tickets. The getTicket-method generates a string that contains the event name and the ticket number as well as the name of the company that created the ticket.

The sample implementation of a main-method is shown below - as well as argumentation of the attribute modifiers.

``` java
package org.htwd.pool.o1;

public class TicketGenerator {
    // constant public class string: name of the company
    public static final String COMPANY = "iTicket Sales International Inc.";

    // private constant string: name of the event
    private final String ticketLabel;

    // private int value: the current ticket count
    private int ticketCounter = 0;
    
    ...

   public static void main(String[] args) {

        System.out.println(TicketGenerator.COMPANY);
        System.out.println("================================================\n");

        TicketGenerator g1 = new TicketGenerator("Queen_Forever_Wembley2025");
        int i = 23;
        while (i > 0) {
            System.out.println("Got a ticket:\n" + g1.getTicket());
            i--;
        }
        System.out.println("Ticket counter: " + g1.getTicketCounter());
    }
```

| **Learning objective**                         | **Task type**     | **Complexity** |
| ---------------------------------------------- | ----------------- | -------------- |
| classes encapsulate data, modifiers control access | worked-out example | 1 - low   |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) read the Java code
2) understand the attributes and their modifiers as well as the methods
3) explain the attribute modifieres
4) describe the functionality of the class
5) implement the main-method to demonstrate the class

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

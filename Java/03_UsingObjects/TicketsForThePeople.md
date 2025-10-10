Topic: using objects

## Learning Task: Tickets for the People 

The code below shows the Ticket-class and the TicketGenerator-class. Read the given Java-code to get an understanding of it.  
Implement the getTicket-method in the TicketGenerator-class and run the finished program to test it.

**The Ticket class:**
``` java
package org.htwd.pool.o3;

public class Ticket {
    private final String label;
    private final int number;

    public Ticket(String label, int number) {
        this.label = label;
        this.number = number;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.label);
        sb.append(" : ");
        sb.append(this.number);
        return sb.toString();
    }
}
```

**The TicketGenerator class:**
``` java
package org.htwd.pool.o3; 

public class TicketGenerator {
    private int ticketCounter = 0;
    private final String ticketLabel;

    public TicketGenerator(String label) {
        this.ticketLabel = label;
    }

    public Ticket getTicket() {
        // ToDo: implement this method
    }

    public int getTicketCounter() {
        return this.ticketCounter;
    }

    public static void main(String[] args) {
        TicketGenerator g1 = new TicketGenerator("Queen_Forever_Wembley2025");
        int i = 23;
        while (i > 0) {
            System.out.println("Got a ticket: " + g1.getTicket());
            i--;
        }
        System.out.println("Ticket counter: " + g1.getTicketCounter());
    }
}
```

---------------------------------------

### Solution
 
``` java
package org.htwd.pool.o3; 

public class TicketGenerator {
    
    ...

    public Ticket getTicket() {
        this.ticketCounter++;
        Ticket t = new Ticket(this.ticketLabel, this.ticketCounter);
        return t;
    }

    ...

}
``` 


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand concepts of using objects             | completion task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  

#### Learning Activities

1) read the Java code
2) implement the requested getTicket-method
3) run the program to test it

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - Classes and objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  
[tutorialspoint.com: Java - Composition](https://www.tutorialspoint.com/association-composition-and-aggregation-in-java)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

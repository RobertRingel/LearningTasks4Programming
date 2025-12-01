Topic: extension, interface

## Learning Task: Priority tasks need a ranking method

Given is the Java class PriorityTask as shown below. In order to automatically sort various objects of this class it is required to impelemnt the interface Comparable.  

Provide an implementation of Comparable<PriorityTask> by coding to appropriate compareTo-method to rank the objects in ascending sequence.  
Test your implementation by running the finished code.

``` java
package org.htwd.pool.o2;

import java.util.Arrays;

public class PriorityTask extends Task {
    private int priority;

    public PriorityTask(String todo, double hrs, int priority) {
        super(todo, hrs);
        this.setPriority(priority);
    }

    public int getPriority() {
        return this.priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("PriorityTask: ");
        sb.append(super.toString());
        sb.append(" : Prio: ");
        sb.append(this.getPriority());
        return sb.toString();
    }

    public static void main(String[] args) {
        PriorityTask[] todo = { new PriorityTask("Prepare for exam", 10.0, 1),
                                new PriorityTask("Watch TV-News", 2.0, 7),
                                new PriorityTask("Debug Java Projekt", 20.0, 2)};
        Arrays.sort(todo);
        System.out.println("--- Ranked Task List ---");
        for (PriorityTask t : todo) {
            System.out.println(t);
        }
        
    }

   
}

```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o2;

import java.util.Arrays;

public class PriorityTask extends Task implements Comparable<PriorityTask> {
    private int priority;

    ...
    public int compareTo(PriorityTask o) {
        return this.getPriority() - o.getPriority();
    }
    ...
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| implementation of the comparable interface       | conventional task | 1 - low      |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-2: basics of class interfaces 

#### Learning Activities

1) read the given Java code
2) identify the methods of the Comparable interface
3) implement the the compareTo-interface-method
4) test the new class implementation

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 4  
[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)    
[geeksforgeeks.org: Java Comparable Interface](https://www.geeksforgeeks.org/java/comparable-interface-in-java-with-examples/)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 174-176

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0

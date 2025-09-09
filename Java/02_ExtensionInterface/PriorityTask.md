Topic: extension, interface

## Learning Task: Tasks need priorities

Given is the below Task class. Implement an extension of this class that provides a numeric priority to each task. The priority value should be of type int. The PriorityTask class should implement the related get- and set-methods for the priority. A toString-method shall also be implemented.

``` java
package org.htwd.pool.o2;

public class Task {
    private String todo;
    private double durationHrs;
    private boolean finished;

    public Task(String todo, double hrs) {
        this.todo = todo;
        this.durationHrs = hrs;
        this.finished = false;
    }

    public boolean isFinished() {
        return this.finished;
    }

    public void setFinished() {
        this.finished = true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.todo);
        sb.append(" : ");
        sb.append(this.durationHrs);
        sb.append(" hrs : finished: ");
        sb.append(this.isFinished());
        return sb.toString();
    }
}
```

---------------------------------------

### Solution

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
        PriorityTask p1 = new PriorityTask("Prepare for exam", 10.0, 1);
        PriorityTask p2 = new PriorityTask("Watch TV-News", 2.0, 7);
        System.out.println (p1);
        System.out.println (p2);
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| implementation of a class extension              | conventional task | 1 - low      |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-2: basics of class extension 

#### Learning Activities

1) read the requirements of the new class
2) read the given Java code
3) implement the new class as extension of the given class
4) test the new class 

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
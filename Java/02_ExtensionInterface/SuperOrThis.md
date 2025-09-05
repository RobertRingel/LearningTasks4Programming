Topic: extension, interface

## Learning Task: super or this?

The code below shows two Java classes. Read the given code and fill in the gaps(...) with correct "this" or "super" keywords.  
Even in some situations "this" is not required - be explicit and state it.

**The Task class:**
``` java
package org.htwd.pool.o2;

public class Task {
    private String todo;
    private double durationHrs;
    private boolean finished;

    public Task(String todo, double hrs) {
        ... .todo = todo;
        ... .durationHrs = hrs;
        ... .finished = false;
    }

    public boolean isFinished() {
        return ... .finished;
    }

    public void setFinished() {
        this. ... = true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(... .todo);
        sb.append(" : ");
        sb.append(... .durationHrs);
        sb.append(" hrs : finished: ");
        sb.append(...  .isFinished());
        return sb.toString();
    }
}
```

**The PriorityTask class:**
``` java
package org.htwd.pool.o2;

public class PriorityTask extends Task {
    private int priority;

    public PriorityTask(String todo, double hrs, int priority) {
        ... (todo, hrs);
        ... .setPriority(priority);
    }

    public int getPriority() {
        return ... .priority;
    }

    public void setPriority(int priority) {
        ... .priority = priority;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("PriorityTask: ");
        sb.append... .toString());
        sb.append(" : Prio: ");
        sb.append(... .getPriority());
        return sb.toString();
    }

    public static void main(String[] args) {
        PriorityTask t = new PriorityTask("Debug Java Projekt", 20.0, 2);
        System.out.println(t);
    }
}
```

---------------------------------------

### Solution

**The Task class:**
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

**The PriorityTask class:**
``` java
package org.htwd.pool.o2;

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
        PriorityTask t = new PriorityTask("Debug Java Projekt", 20.0, 2);
        System.out.println(t);
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| clearly distinguish between this and super       | completion task | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-1: basics of class extension 

#### Learning Activities

1) read the given Java code
2) understand the given code
3) fill in the gaps with "super" or "this"

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
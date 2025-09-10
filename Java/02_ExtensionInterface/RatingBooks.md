Topic: extension, interface

## Learning Task: Rating favourite books

Take the given classes Task and PriorityTask as a kind of blue print for the following task:  
Write a basic book class that has the attributes title and author. Write an extension of this class, that allows to give a rating to book. A rating has a written text or review and a number of stars(1-5). Rated books will implement the Comparable<T> interface to sort them.  

Implement the two classes Book and RatedBook. Test your implementation and demonstrate your classes to another student.

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

import java.util.Arrays;

public class PriorityTask extends Task implements Comparable<PriorityTask> {
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

    public int compareTo(PriorityTask o) {
        return this.getPriority() - o.getPriority();
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

**The Book class:**
``` java
package org.htwd.pool.o2;

public class Book {
    private final String title;
    private final String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public String getTitle() { return this.title; }
    public String getAuthor() { return this.author; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.author);
        sb.append(" : ");
        sb.append(this.title);
        return sb.toString();
    }
}
```

**The RatedBook class:**
``` java
package org.htwd.pool.o2;

import java.util.Arrays;

public class RatedBook extends Book implements Comparable<RatedBook> {
    private String rating;
    private int stars;

    public RatedBook(String title, String author) {
        super(title, author);
        this.rating = "";
        this.stars = 0;
    }

    public boolean giveRating(String rating, int stars) {
        if (stars >=0 && stars <=5 ) {
            this.stars = stars;
            this.rating = rating;
            return true;
        }
        return false;
    }

    public int getStars() {
        return this.stars;
    }

    public String getRating() {
        return this.rating;
    }

    public int compareTo(RatedBook other) {
        // descending sequence!
        return other.getStars() - this.getStars();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append(" : Stars:");
        sb.append(this.getStars());
        sb.append("\n");
        sb.append(this.getRating());
        return sb.toString();
    }

    public static void main(String[] args) {
        RatedBook b1 = new RatedBook("Pride and Prejudice", "Jane Austen");
        b1.giveRating("must read!", 4);
        RatedBook b2 = new RatedBook("The Gambler", "Fyodor Dostoevsky");
        b2.giveRating("a real classic book", 3);
        RatedBook b3 = new RatedBook("The Russia House", "John le Carre");
        b3.giveRating("a thrilling spy novel", 5);
        RatedBook[] books = { b1, b2, b3};
        Arrays.sort(books);
        System.out.println("--- Ranked Book List ---");
        for (RatedBook b : books) {
            System.out.println(b);
        }
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| implementation of class extension and comparable interface | imitation task | 2 - normal |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-1: basics of class extension  
exi-2: basics of class interfaces 

#### Learning Activities

1) read the given Java code
2) implement the Book-class similar to the Task-class
3) implement the RatedBook-class similar to the PriorityTask-class
4) test the implementation
5) demonstrate the classes to another student
6) add-on: compare the own code to the sample solution

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Boxes 3 and 4  
[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)    
[geeksforgeeks.org: Java Comparable Interface](https://www.geeksforgeeks.org/java/comparable-interface-in-java-with-examples/)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
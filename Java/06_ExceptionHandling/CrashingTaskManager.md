Topic: exception handling

## Learning Task: The crashing task manager

The given Java code represents a basic TaskManager that can be used to store tasks and an overall time budget. The implementation is done with help of the [Task-class](Task.java). However, when you run the programm it runs into a crash.  

Read the given code, run it and identify the root cause of the crash. Finally fix the problem with help of a try-catch-block. 

``` java
package org.htwd.pool.o6;

import java.util.ArrayList;

public class TaskManager {

    private ArrayList<Task> tasks = new ArrayList<Task>();
    private int hours = 0;
    public TaskManager() {}

    public void setTime(int t) { this.hours = t; }
    public int getTime() { return this.hours; }

    public void addTask(Task t) { tasks.add(t); }

    public void removeTask(int i) { tasks.remove(i); }

    public void printAllTasks() {
        for (Task t : tasks)
            System.out.println(t);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Total time [hrs]:");
        sb.append(Integer.toString(this.hours));
        sb.append(" Total tasks:");
        sb.append(Integer.toString(tasks.size()));
        sb.append(" avg time/task [hrs]:");
        sb.append(Double.toString(this.hours / tasks.size()));
        return sb.toString();
    }

    public static void main(String[] args) {
        TaskManager tm = new TaskManager();
        tm.setTime(15);
        System.out.println(tm);
        tm.addTask(new Task("Clean kitchen", 1.0));
        tm.addTask(new Task("Buy food", 0.5));
        System.out.println(tm);
        tm.printAllTasks();
    }
}
``` 

---------------------------------------

### Solution

``` java
public class TaskManager {
    ...
    public String toString() {
        StringBuilder sb = new StringBuilder("Total time [hrs]:");
        sb.append(Integer.toString(this.hours));
        sb.append(" Total tasks:");
        sb.append(Integer.toString(tasks.size()));
        sb.append(" avg time/task [hrs]:");
        try {
            sb.append(Double.toString(this.hours / tasks.size()));
        } catch (ArithmeticException e)
        {
            sb.append("---");
        }
        return sb.toString();
    }

}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
col-1: basics of an ArrayList class  
exc-1: basics of exception-handling

#### Learning Activities

1) read and run the given Java code
2) identify the root-cause of the crash  
3) fix the problem with help of a try-catch-block   

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

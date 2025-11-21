Topic: exception handling

## Learning Task: The ToDo list

The given Java program can be used to maintain a personal task list.  

Read and run the program to obtain an understanding of its implementation. Provide a brief written explanation with focus on the addTask and the validateDateTime methods. What is the purpose of the try-catch exception handling in this code?

``` java
package org.htwd.pool.o6;

import java.time.LocalDateTime;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;

public class TaskList {

    private ArrayList<String> todo = new ArrayList<String>();

    public TaskList() {}

    private static boolean validateDateTime(String datetimestr) {
        boolean result = true;
        try {
            LocalDateTime.parse(datetimestr);
        } catch (DateTimeParseException e) {
            result = false;
        }
        return result;
    }

    public void addTask(String date, String time, String task) {
        if (time=="")
            time ="00:00";
        String datetimestr = date+"T"+time+":00";
        if (TaskList.validateDateTime(datetimestr) == false) {
            System.out.println("invalid date-time-information: "+datetimestr+" task rejected: "+task);
            return;
        }
        String job = datetimestr+"\t"+task;
        this.todo.add(job);
    }

    public void removeTask(int idx) {
        if (idx>=0 && idx<this.todo.size())
            this.todo.remove(idx);
    }

    public void printAll() {
        this.todo.sort(String::compareToIgnoreCase);
        int i = 0;
        for (String t : this.todo) {
            System.out.println(i + ") " + t);
            i = i + 1;
        }
    }

    public static void main(String[] args) {
        TaskList t = new TaskList();
        t.addTask("2025-12-21", "10:00", "Python class");
        t.addTask("2025-12-30", "", "Prepare Java exam");
        t.addTask("2025-12-21", "08:00", "Java class");
        t.addTask("2025-12-32", "", "Prepare Physics exam");
        t.printAll();
    }
}
``` 

---------------------------------------

### Solution

The TaskList-class uses an ArrayList to store strings containing ToDo-tasks. A task string consists of a DateTime string (format: YYYY-MM-DD HH:MM:00) and the task note. The class provides methods to add a task, to remove a task and to print a sorted list of all tasks. Addtionally the class provides an internal static method named "validateDateTime" that is used to validate the correct format of a given date-time-string. The implementation uses the LocalDateTime.parse-method to validate the given string. In case the parse-method runs into a DateTimeParseException, the string represents an invalid date-time-information and the method will return false. This check gets performed whenever a new task will be added in order validate the given date and time information.


| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| understand exception handling in problem solving | worked-out example | 1 - low       | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
col-1: basics of the ArrayList class  
exc-1: basics of exception-handling

#### Learning Activities

1) read and run the given Java class 
2) write a brief explanation with focus on the named methods to understand the use of exception handling   

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
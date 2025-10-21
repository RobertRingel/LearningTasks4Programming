Topic: storing objects in collections

## Learning Task: The ToDo-List

Given is the following Java class GPSTrack. Read and run the code to obtain an understanding.  

Use this code as a blueprint to implement the class TaskList to store [PriorityTask-objects](../02_ExtensionInterface/PriorityTask.md) using an ArrayList. Design, implement and test the Java TaskList-class.

Add-on feature: Adding a new task shall be implemented in a way, to keep the task list ranked by the tasks priority.

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.GPSPoint;
import java.util.ArrayList;

public class GPSTrack {
    private ArrayList<GPSPoint> track = new ArrayList<GPSPoint>();

    public GPSTrack() { }

    public void addPoint(double lat, double lon) {
        GPSPoint p = new GPSPoint(lat, lon);
        track.add(p);
    }

    public boolean removePoint(int i) {
        if (i<0 || i> track.size())
            return false;
        track.remove(i);
        return true;
    }

    public GPSPoint getPoint(int i) {
        if (i<0 || i> track.size())
            return null;
        return track.get(i);
    }

    public int size() {
        return track.size();
    }

    public static void main(String[] args) {
        GPSTrack t = new GPSTrack();
        t.addPoint(52.123, 12.01);
        t.addPoint(52.124, 12.00);
        t.addPoint(52.125, 12.01);
        t.addPoint(52.126, 12.03);
        int n = t.size();
        int i = 0;
        while (i<n) {
            GPSPoint p = t.getPoint(i);
            i++;
            System.out.println(p);
        }

        t.removePoint(1);
        System.out.println(t.size());
    }
}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.PriorityTask;

import java.util.ArrayList;
import java.util.Collections;

public class TaskList {

    private ArrayList<PriorityTask> tasks = new ArrayList<PriorityTask>();

    public TaskList() {}

    public void addTask(String todo, double hours, int prio) {
        PriorityTask p = new PriorityTask(todo, hours, prio);
        tasks.add(p);
        Collections.sort(tasks);
    }

    public boolean removeTask(int i) {
        if (i<0 || i>tasks.size())
            return false;
        tasks.remove(i);
        return true;
    }

    public PriorityTask getTask(int i) {
        if (i<0 || i>tasks.size())
            return null;
        return tasks.get(i);
    }

    public int size() {
        return tasks.size();
    }

    public static void main(String[] args) {
        TaskList t = new TaskList();
        t.addTask("Clean kitchen", 1.0, 3);
        t.addTask("Buy food", 0.5,1);
        t.addTask("Prepare presentation", 3.0, 2);
        int n = t.size();
        int i = 0;
        while (i<n) {
            PriorityTask p = t.getTask(i);
            i++;
            System.out.println(p);
        }

        t.removeTask(0);
        System.out.println(t.size());
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the ArrayList collection class | imitation task | 2 - normal    | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the ArrayList class

#### Learning Activities

1) read the given Java code
2) run the program
3) design and implement the requested TaskList class
4) run and test the TaskList class
5) implement and test the add-on feature to keep the list ranked after addinga new task

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0
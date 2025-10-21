Topic: storing objects in collections

## Learning Task: GPS locations

Given is the following Java class GPSLocations. Read and run the code to obtain an understanding.  

Write the related programming task that yields the given Java class.

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.GPSPoint;

import java.util.ArrayList;
import java.util.HashMap;

public class GPSLocations {

    HashMap<String, GPSPoint> locations = new HashMap<String, GPSPoint>();

    public GPSLocations() {}

    public void add(String name, GPSPoint point) {
        locations.put(name, point);
    }

    public void add(String name, double lat, double lon) {
        GPSPoint p = new GPSPoint(lat, lon);
        add(name, p);
    }

    public GPSPoint get(String name) {
        return locations.get(name);
    }

    public void remove(String name) {
        locations.remove(name);
    }

    public ArrayList<String> getAllLocationNames() {
        ArrayList<String> loc = new ArrayList<String>(locations.keySet());
        return loc;
    }

    public static void main(String[] args) {
        GPSLocations locs = new GPSLocations();
        locs.add("HTWD", 51.03779, 13.73502);
        locs.add("Dresden Central Station", 51.04021, 13.73199);
        locs.add("Blue Wonder Bridge",51.05332, 13.80990);

        GPSPoint p = locs.get("HTWD");
        System.out.println("HTWD:" + p);

        locs.remove("Dresden Central Station");
        
        System.out.println("----- List of locations -----");
        ArrayList<String> names = locs.getAllLocationNames();
        for (String n : names) {
            p = locs.get(n);
            System.out.println(n + ": " + p);
        }
    }
}
```

---------------------------------------

### Solution

**Text of the programming task**   
Design and implement the Java class GPSLocations. The class shall be used to store GPSPoint objects in a HashMap to be accessed by the name of location related to the GPSPoint. The class shall provide methods to add a new GPSPoint and its name, to remove a GPSPoint by its name and to get a stored the GPSPoint by its related name. A method named 'getAllLocationNames' shall provide a list of all the names of the stored GPSPoints. Implement a main method to demonstrate the functionality of this class.


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of HashMap and ArrayList collection classes | reverse task | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of HashMap and ArrayList classes

#### Learning Activities

1) read the given Java code
2) run the program
3) write the text of the related programming task

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - HashMap](https://www.tutorialspoint.com/java/util/java_util_hashmap.htm)  

[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0
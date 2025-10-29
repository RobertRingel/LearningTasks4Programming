Topic: storing objects in collections

## Learning Task: Your Idea

Design, implement and test a Java class (name TaggedLocations.java) that can be used to store various GPS locations under certain tags. The implementation shall be based on a HashMap to store GPSLocation objects. The related classes GPSPoint and GPSLocation are available in this task pool task: [GPSLocation.md](../02_ExtensionInterface/GPSLocation.md).  
The new class shall provide functionality to:  
- add a location by a certain tag
- get a list of all locations stored under a certain tag
- print all locations stored under a certain tag

Implement a main-method to demonstrate the functionality of the new class. 
Finally explain you code to another student.

Potential GPS locations a related tags are:  
- tag: Dresden: 52.05, 13.81, Blue Wonder Bridge; 51.04, 13.73, University of Applied Sciences  
- tag: History: 52.05, 13.81, Blue Wonder Bridge

``` java
public class GPSLocation extends GPSPoint {
    private final String name;

    public GPSLocation(double lat, double lon, String name) {
        super(lat, lon);
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append(" : ");
        sb.append(super.toString());
        return sb.toString();
    }

    public static void main(String[] args) {
        GPSLocation loc = new GPSLocation(52.05, 13.81, "Blue Wonder Bridge");
        System.out.println(loc);
    }
}
``` 

---------------------------------------

### Solution

``` java
import java.util.ArrayList;
import java.util.HashMap;

public class TaggedLocations {

    private HashMap<String, ArrayList<GPSLocation>> locations = new HashMap<String, ArrayList<GPSLocation>>();

    public TaggedLocations() { }

    public void addLocation(String tag, GPSLocation loc) {
        if (locations.containsKey(tag)) {
            locations.get(tag).add(loc);
            return;
        }
        ArrayList<GPSLocation> alist = new ArrayList<GPSLocation>();
        alist.add(loc);
        locations.put(tag, alist);
    }

    public ArrayList<GPSLocation> getByTag(String tag) {
        return locations.get(tag);
    }

    public void printByTag(String tag) {
        for (GPSLocation l : locations.get(tag)) {
            System.out.println(l);
        }
    }

    public static void main(String[] args) {
        GPSLocation l1 = new GPSLocation(52.05, 13.81, "Blue Wonder Bridge");
        GPSLocation l2 = new GPSLocation(51.04, 13.73, "University of Applied Sciences Dresden");

        TaggedLocations locs = new TaggedLocations();
        locs.addLocation("Dresden", l1);
        locs.addLocation("Dresden", l2);
        locs.addLocation("History", l1);
        locs.addLocation("Future", l2);

        locs.printByTag("Dresden");
        ArrayList<GPSLocation> loclist = locs.getByTag("Future");
        System.out.println(loclist.get(0));
    }
}
``` 


| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the HashMap and ArrayList collection classes | conventional task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the ArrayList and HashMap classes

#### Learning Activities

1) read and understand the requirements of the new class  
2) design and implement the new class TaggedLocations  
3) test and run the new class based on an appropriate main-method
4) explain the Java program to another student

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

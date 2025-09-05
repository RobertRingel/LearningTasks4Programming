Topic: extension, interface

## Learning Task: A GPS location point

The code below shows two Java classes. The firt class GPSPoint was given - the second class GPSLocation was to be developed. Read and run the code to obtain an understanding. 

Write the text of a programming task that requests to develop the class GPSPoint.

**The given GPSPoint class:**
``` java
package org.htwd.pool.o2;

public class GPSPoint {
    private double lon;
    private double lat;

    public GPSPoint(double lat, double lon) {
        this.lat = lat;
        this.lon = lon;
    }

    public double getLatitude() {
        return this.lat;
    }

    public double getLongitude() {
        return this.lon;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Lat:");
        sb.append(this.lat);
        sb.append(" : Lon:");
        sb.append(this.lon);
        return sb.toString();
    }
}
```

**The requested GPSLocation class:**
``` java
package org.htwd.pool.o2;

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

The text of the programming task:

Given is the source code of the GPSPoint-class. Develop a class named "GPSLocation" as extension of the GPSPoint-class. The new class shall contain an attribute to name the location. This attribute shall be unchangable after it was set be the constructor. A toString-method is also requested for the new class. Its implementation shall use the super.toString-method and it shall also provide the location name. Code a very short main-method to demonmstrate the class GPSLocation.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply basic features of inheritance in Java      | reverse task  | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-1: basics of class extension 

#### Learning Activities

1) read the given Java code
2) run the given code
3) write the text of the requested programming task for class GPSLocation

#### Supporting information

Java-OOP-Poster: Box 3

[tutorialspoint.com: Java - Inheritance](https://www.tutorialspoint.com/java/java_inheritance.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
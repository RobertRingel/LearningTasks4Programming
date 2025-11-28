Topic: storing objects in collections

## Learning Task: The GPS track

Given is the class GPSPoint. Based on this class you should design and implement the class of a GPS track. This class shall store GPSPoint objects using an ArrayList. It should provide functionality to add, remove and get GPSPoints. The remove and get operations shall work based on the GPSPoint index number.

Implement this class in Java and demonstrate its functionality by a main-method implementation.

**The GPSPoint class:**
``` java
package org.htwd.pool.o4;

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

---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class GPSTrack {
    private ArrayList<GPSPoint> track = new ArrayList<GPSPoint>();

    public GPSTrack() { }

    public void addPoint(double lat, double lon) {
        GPSPoint p = new GPSPoint(lat, lon);
        track.add(p);
    }

    public void addPoint(GPSPoint p) {
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

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of an ArrayList collection class | conventional task   | 1 - low   |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of an ArrayList class

#### Learning Activities

1) read the given Java code
2) design the Java class GPSTrack
3) implement the requested class methods
4) implement the main method to demonstrate the class features
5) test and run the program

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 7, pages 211-232

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0

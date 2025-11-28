Topic: classes, modifiers

## Learning Task: GPS distance calculation

The Java code below models a GPS point located in Germany. Read the code and understand it. Implement the calculateDistance-method to calculate the distance to an other nearby GPS point based on the theorem of Pythagoras. Print a warning, in case the calculated distance violates the defined warning limit. Return -1.0 and print an error message in case one of the GPS points is not located in Germany.

Test your implementation by writing an appropriate main-method.

``` java
package org.htwd.pool.o1;

public class GPSPoint {
    protected final static double MIN_LAT = 47.0;
    protected final static double MAX_LAT = 55.0;
    protected final static double MIN_LON = 5.8;
    protected final static double MAX_LON = 15.0;

    // avg. width of 1 degree latitude in Germany
    protected final static double LAT_WIDTH = 111.3; 
    // avg. width of 1 degree longitude in Germany
    protected final static double LON_WIDTH = 71.5;	 

    protected final static double WARN_LIMIT = 50.0;

    private double latitude;
    private double longitude;

    public GPSPoint(double lat, double lon) {
        this.latitude = lat;
        this.longitude = lon;
    }

    public static boolean inGermany(GPSPoint p) {
        if ((p.latitude < GPSPoint.MIN_LAT) || (p.latitude > GPSPoint.MAX_LAT))
            return false;
        if ((p.longitude < GPSPoint.MIN_LON) || (p.longitude > GPSPoint.MAX_LON))
            return false;
        return true;
    }

    public double getLatitude() {
        return this.latitude;
    }

    public double getLongitude() {
        return this.longitude;
    }

    public static double calculateDistance(GPSPoint p1, GPSPoint p2) {
        // TODO: implement this method
    }

}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o1;

public class GPSPoint {
    ...
    public static double calculateDistance(GPSPoint p1, GPSPoint p2) {
        if (GPSPoint.inGermany(p1) && GPSPoint.inGermany(p2)) {
            double dx = LON_WIDTH * (p1.getLongitude() - p2.getLongitude());
            double dy = LAT_WIDTH * (p1.getLatitude() - p2.getLatitude());
            double dist = Math.sqrt(dx * dx + dy * dy);
            if (dist > GPSPoint.WARN_LIMIT)
                System.out.println("Distance accuracy warning due to distance limit violation.");
            return dist;
        }
        System.out.println("Error: At least one point is outside Germany.");
        return -1.0;
    }

    public static void main(String[] args) {
        GPSPoint p1 = new GPSPoint(52.0, 14.0);
        GPSPoint p2 = new GPSPoint(52.0, 14.1);
        double d = GPSPoint.calculateDistance(p1,p2);
        System.out.println("Distance [km]: "+d);
    }
}
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| make use of static methods and attributes      | completion task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes, static modifier  

#### Learning Activities

1) read the Java code
2) implement the requested method
3) implement a main method to test the implementation
4) run the code and test it

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 134-156

Information about GPS calculations (German language): [https://www.kompf.de/gps/distcalc.html](https://www.kompf.de/gps/distcalc.html)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

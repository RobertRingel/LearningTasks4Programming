Topic: extension, interface

## Learning Task: The GPS-TrackPoint

The code below shows an interface class and a Java class to implement the interface.
Read the code to understand it.   

Add two more methods to the Trackable-interface. The methods should provide the current latitude and the current longitude as double values. Update the GPSTrackPoint-class accordingly and implement a main-method to demonstrate the updated class code.

**The interface class Trackable:**
``` java
package org.htwd.pool.o2;

public interface Trackable {
    public String currentLocationString();
}
```

**The GPSTrackPoint class:**
``` java
package org.htwd.pool.o2;

public class GPSTrackPoint implements Trackable {

    private double latitude;
    private double longitude;

    public GPSTrackPoint(double lat, double lon) {
        this.update(lat, lon);
    }

    public boolean update(double lat, double lon) {
        if (lat >= -90.0 && lat<= 90.0 && lon>=-180.0 && lon<=180.0) {
            this.latitude = lat;
            this.longitude = lon;
            return true;
        }
        return false;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Lat:");
        sb.append(this.latitude);
        sb.append(" : Lon:");
        sb.append(this.longitude);
        return sb.toString();
    }

    public String currentLocationString() {
        return this.toString();
    }
}
```

---------------------------------------

### Solution

**The interface class Trackable:**
``` java
package org.htwd.pool.o2;

public interface Trackable {
    public String currentLocationString();
    public double getLatitude();    // <<<<< new
    public double getLongitude();   // <<<<< new
}
```

**The GPSTrackPoint class:**
``` java
package org.htwd.pool.o2;

public class GPSTrackPoint implements Trackable {

    private double latitude;
    private double longitude;

    public GPSTrackPoint(double lat, double lon) {
        this.update(lat, lon);
    }

    public boolean update(double lat, double lon) {
        if (lat >= -90.0 && lat<= 90.0 && lon>=-180.0 && lon<=180.0) {
            this.latitude = lat;
            this.longitude = lon;
            return true;
        }
        return false;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Lat:");
        sb.append(this.latitude);
        sb.append(" : Lon:");
        sb.append(this.longitude);
        return sb.toString();
    }

    public String currentLocationString() {
        return this.toString();
    }

    public double getLatitude() { return this.latitude; }   // <<<<< new

    public double getLongitude() {return this.longitude; }  // <<<<< new

    public static void main(String[] args) {
        GPSTrackPoint p = new GPSTrackPoint(52.1, 13.2);
        double lat = p.getLatitude();
        double lon = p.getLongitude();
        System.out.println(lat+" "+lon);
        System.out.println("Current location: " +p.currentLocationString());
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| update an interface and its related implementation | completion task | 1 - low      |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-2: basics of interface definition and implementation 

#### Learning Activities

1) read the given Java code
2) run the given code
3) write a brief description of the consume-methods 

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 4

[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
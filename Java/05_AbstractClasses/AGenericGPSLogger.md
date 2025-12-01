Topic: abstract classes

## Learning Task: A generic GPS logger

Read and run the Java code of the two given classes.  
Write the according task description that yields then given code of the two classes.  

``` java
package org.htwd.pool.o5;

public abstract class AbstractGPSLogger {

    public AbstractGPSLogger(){}

        abstract public Object startLogging();

        abstract public boolean stopLogging();implement a main-Method to demonstrate the CookieVoucher  

        abstract public boolean logTrackPoint(double lat, double lon, String note);
}implement a main-Method to demonstrate the CookieVoucher  
``` 

``` java
package org.htwd.pool.o5;

import java.time.LocalTime;
import java.util.ArrayList;

public class GPSListLogger extends AbstractGPSLogger {
    private ArrayList<String> trackList = null;
    private final String DELIMITER = "\t";
    public GPSListLogger() { }

    @Override
    public Object startLogging() {
        trackList = new ArrayList<String>();
        return trackList;
    }

    @Override
    public boolean stopLogging() {
        return true;
    }

    @Override
    public boolean logTrackPoint(double lat, double lon, String note) {
        LocalTime locTime = LocalTime.now();
        String strPoint = locTime.toString() + DELIMITER + Double.toString(lat) + DELIMITER + Double.toString(lon) + DELIMITER + note;
        trackList.add(strPoint);
        return true;
    }

    public static void main(String[] args) {
        GPSListLogger l = new GPSListLogger();
        ArrayList<String> list = (ArrayList<String>)l.startLogging();
        l.logTrackPoint(52.123, 9.456, "Start");
        l.logTrackPoint(52.124, 9.457, "");
        l.logTrackPoint(52.125, 9.458, "End");
        l.stopLogging();
        for (String p : list)
            System.out.println(p);
    }
}
``` 

---------------------------------------

### Solution

Design a Java class that models a generic approach for GPS logging. It should support start logging, adding annotated GPS coordinates and it should support stop logging. The class name should be AbstractGPSLogger. Implement this class as an abstract class, that is open for different logging techniques.  
Design and implement a second class that is an extension of the AbstractGPSLogger. This class shall perform the logging with help of an ArrayList of strings. Implement a main method to demonstrate the functionality of this class.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the idea of abstract classes          | reverse task    | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
col-1: basics of an ArrayList class  
exi-1: basics of class extension  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) run the Java code to manifest the understanding   
3) write the related programming task  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 172-174

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

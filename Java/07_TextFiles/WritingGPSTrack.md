Topic: text files

## Learning Task: Writing a GPS track

The following Java class is used to store GPS co-ordinates of a potential GPS track. It makes use of the [GPSPoint-class](GPSPoint.java). The sequence of GPSPoints can be written to a text file with help of the writeToFile-method. The resulting text file is shown as a demo here:  
``` java
52.123;12.01
52.124;12.0
52.125;12.01
52.126;12.03
```

Read and run the given Java program. Add line comments to the implementation of the writeToFile-method to document your understanding of the code. Compare your result with the one of another student.

``` java
package org.htwd.pool.o7;

import java.io.*;
import java.util.ArrayList;

public class GPSTrack {
    private ArrayList<GPSPoint> track = new ArrayList<GPSPoint>();
    private final String DELIMITER = ";";

    public GPSTrack() { }

    public void writeToFile(String filename) {
        try {
            FileWriter writer = new FileWriter(filename, false);
            for (GPSPoint p : this.track) {
                double lat = p.getLatitude();
                double lon = p.getLongitude();
                String line = lat+DELIMITER+lon+"\n";
                writer.write(line);
            }
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing track file: "+e.getMessage());
        }
    }

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
        t.writeToFile("track01.txt");
    }
}
```

---------------------------------------

### Solution

``` java
    public void writeToFile(String filename) {
        try {
            FileWriter writer = new FileWriter(filename, false);  // FileWriter will create the new text file
            for (GPSPoint p : this.track) {                       // iterate all points of the  track-list 
                double lat = p.getLatitude();                     // get latitude value
                double lon = p.getLongitude();                    // get longitude value
                String line = lat+DELIMITER+lon+"\n";             // create text file line - use DELIMITER
                writer.write(line);                               // write line to the file
            }
            writer.close();                                       // close text file
        } catch(IOException e) {                                  // catch and handle IOExceptions
            System.out.println("Error writing track file: "+e.getMessage());
        }
    }
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| understand text file reading                     | worked-out example | 1 - low       |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling  
txt-1: basics of text file reading  

#### Learning Activities

1) read and run the given Java program  
2) write line comments to the writeToFile-method  
3) compare the line commentes with the ones of another student  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
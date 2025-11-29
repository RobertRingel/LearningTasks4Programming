Topic: text files

## Learning Task: Reading a GPS track

The following Java class is used to store GPS co-ordinates of a potential GPS track. It makes use of the [GPSPoint-class](GPSPoint.java). The sequence of GPSPoints can be read from a text file with help of the loadFromFile-method. The related text file is shown as a demo here:  
``` java
52.123;12.01
52.124;12.0
52.125;12.01
52.126;12.03
```

Read and run the given Java program. Add line comments to the implementation of the loadFromFile-method to document your understanding of the code. Compare your result with the one of another student.

``` java
package org.htwd.pool.o7;

import java.io.*;
import java.util.ArrayList;

public class GPSTrack {
    private ArrayList<GPSPoint> track = new ArrayList<GPSPoint>();
    private final String DELIMITER = ";";

    public GPSTrack() { }

    public void loadFromFile(String filename) {
        String line;
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            while ((line = br.readLine()) != null) {
                String[] token = line.split(DELIMITER);
                if (token.length != 2)
                    throw new RuntimeException("corrupt line:" + line);
                double lat = Double.parseDouble(token[0].strip());
                double lon = Double.parseDouble(token[1].strip());
                this.addPoint(lat, lon);
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found:" + filename);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (RuntimeException e) {
            System.out.println("Error while reading a file:" + e.getMessage());
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
        t.loadFromFile("track01.txt");

        int n = t.size();
        int i = 0;
        while (i<n) {
            GPSPoint p = t.getPoint(i);
            i++;
            System.out.println(p);
        }
    }
}
```

---------------------------------------

### Solution

``` java
    public void loadFromFile(String filename) {
        String line;
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {  // create a text file reader object
            while ((line = br.readLine()) != null) {                              // read all the file line by line   
                String[] token = line.split(DELIMITER);                           // split line based on DELIMITER
                if (token.length != 2)                                            // illegal number of line items?
                    throw new RuntimeException("corrupt line:"+line);             // throw exception show the corrupt line 
                double lat = Double.parseDouble(token[0].strip());                // convert line item to double as latitude
                double lon = Double.parseDouble(token[1].strip());                // convert line item to double as longitude 
                this.addPoint(lat, lon);                                          // add new track point 
            }
            br.close();                                                           // close file reader
        } catch (FileNotFoundException e) {                                       // catch and handle file not found
            System.out.println("File not found:"+filename);
        } catch (IOException e) {                                                 // catch and handle IOException
            throw new RuntimeException(e);
        } catch (RuntimeException e) {                                            // catch and handle RunTimeException
            System.out.println("Error while reading a file:"+e.getMessage());
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
2) write line comments to the loadFromFile-method  
3) compare the line commentes with the ones of another student  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

Topic: text files

## Learning Task: Logging all ticket sales

Given is the below Java program that is able to write a sequence of GPSPoint-objects to a text file. Read the code and understand the implementation. Use the given code as an implementation blueprint for a similar class, that is able to write tickets, that have been genrated by the TicketGenerator, into a log file.

The implementation shall be based on the TicketGenerator-class given in the solution part of the task ["Printing tickets"](../01_ClassesModifier/TicketGenerator.md).  
Every line that gets written to the log file shall start with a current time stamp in the format of: yyyy-MM-dd HH:mm:ss  

Implement this Java program and do not forget to test it.

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

Note: Here is the Java code to get a String containing the current time stamp:

``` java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

LocalDateTime now = LocalDateTime.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String TimeStamp = now.format(formatter);
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o7;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class TicketGenerator {
    private static final String COMPANY = "iTicket Sales International Inc.";
    private final String LOGFILENAME = "tickets.log";
    private final String ticketLabel;
    private int ticketCounter = 0;


    public TicketGenerator(String label) {
        this.ticketLabel = label;
    }

    public String getTicket() {
        this.ticketCounter++;
        String ticket = this.ticketLabel + ":" + this.ticketCounter;
        ticket = ticket + "\n" + TicketGenerator.COMPANY;
        this.writeLogEntry(ticket);
        return ticket;
    }

    public void writeLogEntry(String ticket) {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String TimeStamp = now.format(formatter);

        try {
            FileWriter writer = new FileWriter(LOGFILENAME, true);
            String line = TimeStamp+"\n"+ticket+"\n";
            writer.write(line);
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing log file: "+e.getMessage());
        }
    }

    public int getTicketCounter() {
        return this.ticketCounter;
    }

    public static void main(String[] args) {
        TicketGenerator g = new TicketGenerator("Queen_Forever_Wembley2025");
        int i = 23;
        while (i > 0) {
            System.out.println("Got a ticket:\n" + g.getTicket());
            i--;
        }
        System.out.println("Ticket counter: " + g.getTicketCounter());
    }
}
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file writing                          | imitation task    | 2 - normal     |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of an ArrayList class  
exc-1: basics of exception-handling  
txt-1: basics of text file writing  

#### Learning Activities

1) read and run the given Java program  
2) read the TicketGenerator class that will be the bases of the implementation  
3) implement the log file writing to the TicketGenerator class  
4) test the program  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

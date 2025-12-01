Topic: text files

## Learning Task: My favourite books

Given is the below Java program that is able to read a GPS track from a text file and to create the according sequence of GPSPoint objects. Read the code and understand the implementation. Use the given code as an implementation blueprint for a similar class that is able to read a list of your favourite books out of a text file and to create the related RatedBooks objects in an ArrayList. The structure of the text file shall be:
```
--- example lines --- 
Robert Harris;Enigma;****;great, authentic, must read for computer science students
Mark Twain;Tom Sawyer
--- valid line patterns --- 
<author>;<title>;<stars>;<brief rating text>
<author>;<title>
```

The implementation shall be done with help of the RatedBooks-class that is given in the solution part of the task ["Rating favourite books"](../02_ExtensionInterface/RatingBooks.md).  
Finally test your program for valid and invalid file formats.

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
package org.htwd.pool.o7;

import org.htwd.pool.o2.RatedBook;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class BestBooks {
    private static final String DELIMITER = ";";
    private ArrayList<RatedBook> books = new ArrayList<RatedBook>();

    public BestBooks() { }

    public void add(String author, String title, String rating, int stars) {
        RatedBook b = new RatedBook(title, author);
        if (rating!="" && stars >= 0)
            b.giveRating(rating, stars);
        this.books.add(b);
    }

    public void listAll() {
        for (RatedBook b : this.books) {
            System.out.println(b);
        }
    }

    public void loadFromFile(String filename) {
        String line;
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            while ((line = br.readLine()) != null) {
                String[] token = line.split(DELIMITER);
                if (token.length != 4 && token.length != 2)
                    throw new RuntimeException("corrupt line:" + line);
                String author = token[0].strip();
                String title = token[1].strip();
                int rate = -1;
                String rating = "";
                if (token.length == 4) {
                    String stars = token[2].strip();
                    rate = stars.length();
                    rating = token[3].strip();
                }
                this.add(author, title, rating, rate);
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

    public static void main(String[] args) {
        BestBooks bb = new BestBooks();
        bb.loadFromFile("BestBooks.txt");
        bb.listAll();
    }
}
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file reading                          | imitation task    | 2 - normal     |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
uob-1: basics of creating and using objects  
col-1: basics of an ArrayList class  
exc-1: basics of exception-handling  
txt-2: basics of text file reading  

#### Learning Activities

1) read and run the given Java program  
2) understand its implementation - explain it to another person  
3) write a similar Java program to manage your favourite books  
4) test the program for valid and invalid file formats  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

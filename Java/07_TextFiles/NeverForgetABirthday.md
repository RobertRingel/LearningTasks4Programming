Topic: text files

## Learning Task: Never forget a birthday

Given is the class DaysDiff that provides a static method to calculate the difference in days between a given date and today's date. In case the given date is past, the returned number of days will be negative.  

Based on this calculation approach you should develop a Java class Birthday-checker that reads a text file of person names and birthdays. The class shall print all person names, who's birthdays are within a given range of days from today.  

That file format might be like this:

```
Steffen Fischer;1970-12-01
Thomas Krause;1974-08-04
```

``` java
package org.htwd.pool.o7;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import static java.lang.Math.abs;

public class DaysDiff { 

    public static long getDayDiffToday(String strDate, String format) throws ParseException {
        // days in the past will return a negative number - format e,g.: yyyy-MM-dd
        Date today = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat(format); 
        Date date = sdf.parse(strDate);
        long diffInMillies = date.getTime() - today.getTime();
        long diff = TimeUnit.DAYS.convert(diffInMillies, TimeUnit.MILLISECONDS);
        return diff;
    }
}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o7;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import static java.lang.Math.abs;

public class BirthdayChecker { 
    private final String DELIMITER = ";";
    private final String filename;

    public BirthdayChecker(String filename) {
        this.filename = filename;
    }

    public static long getDayDiffToday(String strDate, String format) throws ParseException {
        // days in the past will return a negative number
        Date today = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat(format);  // format e,g.: yyyy-MM-dd
        Date date = sdf.parse(strDate);
        long diffInMillies = date.getTime() - today.getTime();
        long diff = TimeUnit.DAYS.convert(diffInMillies, TimeUnit.MILLISECONDS);
        return diff;
    }

    public void check(int daydiff) {
        String line = "";
        String currYear = new SimpleDateFormat("yyyy").format(new Date());

        try {
            try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
                while ((line = br.readLine()) != null) {
                    String[] token = line.strip().split(DELIMITER);
                    if (token.length != 2) {
                        throw new RuntimeException("corrupt line:"+line);
                    }
                    String bday = token[1];
                    bday = currYear+"-"+bday.substring(5);
                    long diff = BirthdayChecker.getDayDiffToday(bday, "yyyy-MM-dd");
                    if (abs(diff) <= daydiff) {
                        System.out.println(line);
                    }
                }
                br.close();
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found:"+filename);
        } catch (RuntimeException | IOException e) {
            System.out.println("Error while reading a file:" + e.getMessage());
        } catch (ParseException e) {
            System.out.println(line+":"+e.getMessage());
        }
    }

    public static void main(String[] args) {
        BirthdayChecker bc = new BirthdayChecker("birthdays.txt");
        bc.check(5);
    }
}
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file reading in problem solving       | conventional task | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
uob-1: basics of creating and using objects  
exc-1: basics of exception-handling  
txt-2: basics of text file reading  

#### Learning Activities

1) read the given Java program  
2) develop a the BirthdayChecker class  
3) test the program  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

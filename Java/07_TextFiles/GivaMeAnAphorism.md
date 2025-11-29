Topic: text files

## Learning Task: Give me an aphorism

The following Java program presents you random aphorisms. Read and run the program. Then write a programming task that yields this Java program.

``` java
package org.htwd.pool.o7;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class RandomAphorism {

    private ArrayList<String> aphorisms = new ArrayList<String>();
    private final String DELIMITER = "-";

    public RandomAphorism(String filename) {
        readFromFile(filename);
    }

    private void readFromFile(String filename) {
        String line;
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            StringBuilder phrase = new StringBuilder("");
            while ((line = br.readLine()) != null) {
                if (line.strip().startsWith(DELIMITER)) {
                    aphorisms.add(phrase.toString());
                    phrase = new StringBuilder("");
                } else {
                    phrase.append(line.strip()+"\n");
                }
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found:"+filename);
        } catch (RuntimeException | IOException e) {
            System.out.println("Error while reading a file:" + e.getMessage());
        }
    }

    public void showOne() {
        Random r = new Random();
        int n = this.aphorisms.size();
        int idx = r.nextInt(n);
        System.out.println(this.aphorisms.get(idx));
    }

    public static void main(String[] args) {
        RandomAphorism ra = new RandomAphorism("aphorism.txt");
        ra.showOne();
        ra.showOne();
    }
}
```

---------------------------------------

### Solution

Write a Java class that can be used to print randomly choosen aphorism texts. The texts shall be read from a text file. One aphorism can extend over multiple lines. A line that has a minus character at line start will be used as a separator for aphorism texts.

The aphorism sample file is ["aphorism.txt"](aphorism.txt).

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| understand text file reading                     | reverse task      | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling  
txt-1: basics of text file reading  

#### Learning Activities

1) read and run the given Java program  
2) understand its implementation  
3) write the text of the related programming task  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

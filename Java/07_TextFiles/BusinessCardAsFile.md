Topic: text files

## Learning Task: Business Card as file

The following Java class is a program to design and print business cards. It is based on the [AbstractBusinessCard-class](AbstractBusinessCard.java). Read the code and run it to understand its implementation.

Add a method named "printCardToFile(String filename)" that is able to print the business card into a text file.
Compare your implementation to the one give in the sample solution.

``` java
package org.htwd.pool.o7;

import java.io.FileWriter;
import java.io.IOException;

public class BoxedBusinessCardPrinter extends AbstractBusinessCard {

    private int maxLineLength() {
        int maxLen = 0;
        for (String l : this.lines) {
            if (l.length()>maxLen)
                maxLen = l.length();
        }
        return maxLen;
    }

    public static String getCenteredText(int width, String text) {
        int padding_l = (width - text.length()) / 2;
        int padding_r = padding_l;
        if (padding_l+text.length()+padding_r<width)
            padding_r++;
        String centeredText = String.format("%" + padding_l + "s%s%" + padding_r + "s", "", text, "");
        return centeredText;
    }

    @Override
    public void printCard() {
        System.out.println(this.toString());
    }

    public String toString() {
        int width = 4 + maxLineLength();
        String boundLine = "-".repeat(width+2);
        StringBuilder sb = new StringBuilder(boundLine+"\n");

        for (String l : this.lines) {
            String text = "|" + BoxedBusinessCardPrinter.getCenteredText(width,l) + "|\n";
            sb.append(text);
        }
        sb.append(boundLine+"\n");
        return sb.toString();
    }

    public static void main(String[] args) {
        BoxedBusinessCardPrinter prt = new BoxedBusinessCardPrinter();
        prt.setLine(1,"Bob Miller");
        prt.setLine(2,"The manager");
        prt.setLine(3,"Tasteful Breweries Ltd.");
        prt.showLines();
        prt.printCard();
        // todo: implement the method below
        // prt.printCardToFile("BobMiller.txt");
    }

}
```

---------------------------------------

### Solution

``` java
    public void printCardToFile(String filename) {
        try {
            FileWriter writer = new FileWriter(filename, false);
            writer.write(this.toString());
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing log file: "+e.getMessage());
        }
    }
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file writing                          | completion task   | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
abs-1: basics of abstract classes  
exc-1: basics of exception-handling  
txt-1: basics of text file writing  

#### Learning Activities

1) read and run the given Java program  
2) implement the requested file writing method  
3) test the implementation with help of the main-method  
4) compare the implementation to the sample solution  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

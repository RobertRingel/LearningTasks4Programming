Topic: abstract classes

## Learning Task: Lets print business cards!

We want to print different styles of buisness cards. The given Java class AbstractBusinessCard shall be used as a kind of blue-print for our purpose. We want that every sub-class should implement the printCard-method in a very specific way.  
Read the given Java code to obtain an understanding. Make the printCard-method abstract. Develop a sub-class of the AbstractBusinessCard-class that implements the printing in a very specific fashion - e.g. CapitalBusinessCardPrinter to print all text on the card in capital letters.  

**Add-on task**  
Implement a boxed business card printer that prints box-bound centered text on the card. The Java class [BoxedBusinessCardPrinter](BoxedBusinessCardPrinter.java) provides the required supporting functionality.

 
``` java
package org.htwd.pool.o5;

import java.util.ArrayList;

public class AbstractBusinessCard {     
    protected ArrayList<String> lines = new ArrayList<String>();

    public AbstractBusinessCard() {
        int i=0;
        while (i<8) {
            lines.add("");
            i++;
        }
    }

    public boolean setLine(int line, String text) {
        if ((line<1) || (line>8))
            return false;
        lines.set(line, text);
        return true;
    }

    public void showLines() {
        for (String l : lines)
            System.out.println(l);
    }

    public void printCard() {
        System.out.println("no yet implemented");
    }
}
``` 
---------------------------------------

### Solution

**Example for the abstract generic base class**
``` java
package org.htwd.pool.o5;

import java.util.ArrayList;

public abstract class AbstractBusinessCard {   
 ...

    abstract public void printCard(); 
}
```  

**Example for the CapitalBusinessCardPrinter-class**

``` java
package org.htwd.pool.o5;

public class CapitalBusinessCardPrinter extends AbstractBusinessCard {

    @Override
    public void printCard() {
        for (String l : this.lines) {
            System.out.println(l.toUpperCase());
        }
    }

    public static void main(String[] args) {
        CapitalBusinessCardPrinter prt = new CapitalBusinessCardPrinter();
        prt.setLine(1, "Bob Miller");
        prt.setLine(2, "!the manager!");
        prt.setLine(3, "Tasteful Breweries Ltd.");
        prt.showLines();
        prt.printCard();
    }
}
``` 

**Example for the BoxedBusinessCardPrinter class**

``` java
package org.htwd.pool.o5;

public class BoxedBusinessCardPrinter extends AbstractBusinessCard {

...
    @Override
    public void printCard() {
        int width = 4 + maxLineLength();
        printLine(width);

        for (String l : this.lines) {
            String text = "|" + BoxedBusinessCardPrinter.getCenteredText(width,l) + "|";
            System.out.println(text);
        }
        printLine(width);
    }

    public static void main(String[] args) {
        BoxedBusinessCardPrinter prt = new BoxedBusinessCardPrinter();
        prt.setLine(1,"Bob Miller");
        prt.setLine(2,"!the manager!");
        prt.setLine(3,"Tasteful Breweries Ltd.");
        prt.showLines();
        prt.printCard();
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise abstract classes design and application | completion task  | 2 - normal    | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
col-1: basics of an ArrayList class  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code   
2) adapt the implementation of AbstractBusinessCard to make it an abstract class       
3) implement the CapitalBusinessCardPrinter to print capital letter business cards    
4) implement a main-method to test and demonstrate the functionality  
5) add-on task: implement and test a box-bound business card printer or any other special card printer  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

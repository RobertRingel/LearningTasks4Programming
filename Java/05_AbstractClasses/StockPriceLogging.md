Topic: abstract classes

## Learning Task: Logging stock prices

Read the given Java code of the class AbstractGPSLogger. Inspired by the given implementation you should design and implement an abstract class AbstractStockPriceLogger that defines services to log stock prices. Based on this abstract class you should develop a class that can be used to write stock price loggings including time stamp, stock code and current price into the console. Provide a main-method implementation to demonstrate the functionality of the new class StockPriceConsoleLogger.  

``` java
package org.htwd.pool.o5;

public abstract class AbstractGPSLogger {

    public AbstractGPSLogger(){}

        abstract public Object startLogging();

        abstract public boolean stopLogging();implement a main-Method to demonstrate the CookieVoucher  

        abstract public boolean logTrackPoint(double lat, double lon, String note);
}
``` 

---------------------------------------

### Solution

**The abstract class: AbstractStockPriceLogger**

``` java
package org.htwd.pool.o5;

public abstract class AbstractStockPriceLogger {

    public AbstractStockPriceLogger(){}

    abstract public Object startLogging();

    abstract public boolean stopLogging();

    abstract public boolean logPrice(String StockCode, double price);
}
``` 

**The console logging class: StockPriceConsoleLogger**
``` java
package org.htwd.pool.o5;

import java.time.LocalTime;

public class StockPriceConsoleLogger extends AbstractStockPriceLogger{

    public StockPriceConsoleLogger() {}

    @Override
    public Object startLogging() {
        // no implementation required
        // log will be written directly to console
        return null;
    }

    @Override
    public boolean stopLogging() {
        // no implementation required
        return false;
    }

    @Override
    public boolean logPrice(String StockCode, double price) {
        LocalTime locTime = LocalTime.now();
        System.out.println(locTime.toString() + " " + StockCode + ": " + Double.toString(price));
        return true;
    }

    public static void main(String[] args) {
        StockPriceConsoleLogger log = new StockPriceConsoleLogger();
        log.logPrice("DHL", 44.28);
        log.logPrice("BMW", 85.90);
        log.logPrice("IFX", 33.61);
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise abstract classes design and application | imitation task  | 2 - normal     | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) develop a similar abstract class for stock price logging   
3) implement the console logger class based on the new abstract class  
4) implement a main-method to demonstrate the class functionality  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
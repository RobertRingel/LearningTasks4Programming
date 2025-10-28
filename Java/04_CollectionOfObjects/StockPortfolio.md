Topic: storing objects in collections

## Learning Task: The Stock Portfolio

Given is the following Java class GPSLocations. Read and run the code to obtain an understanding.  

Use this code as a blueprint to implement the class StockPortfolio to store [StockItem-objects](StockItem.java) using a HashMap. Design, implement and test the StockItem-class.

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.GPSPoint;

import java.util.ArrayList;
import java.util.HashMap;

public class GPSLocations {

    HashMap<String, GPSPoint> locations = new HashMap<String, GPSPoint>();

    public GPSLocations() {}

    public void add(String name, GPSPoint point) {
        locations.put(name, point);
    }

    public void add(String name, double lat, double lon) {
        GPSPoint p = new GPSPoint(lat, lon);
        add(name, p);
    }

    public GPSPoint get(String name) {
        return locations.get(name);
    }

    public void remove(String name) {
        locations.remove(name);
    }

    public ArrayList<String> getAllLocationNames() {
        ArrayList<String> loc = new ArrayList<String>(locations.keySet());
        return loc;
    }
}

```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;
import java.util.HashMap;

public class StockPortfolio {

    HashMap<String,StockItem> portfolio = new HashMap<String,StockItem>();

    public StockPortfolio() {}

    public void add(StockItem item) {
        portfolio.put(item.getStockCode(), item);
    }

    public void add(String code, double price, double pcs) {
        StockItem item = new StockItem(code, pcs, price);
        add(item);
    }

    public StockItem get(String code) {
        return portfolio.get(code);
    }

    public void remove(String code) {
        portfolio.remove(code);
    }

    public ArrayList<String> getAllItemCodes() {
        ArrayList<String> codes = new ArrayList<String>(portfolio.keySet());
        return codes;
    }

    public static void main(String[] args) {
        StockPortfolio sp = new StockPortfolio();
        sp.add("IBM", 31.03, 3.0);
        sp.add("AMD", 51.42, 7.0);
        sp.add("SAP",75.05, 2.0);

        StockItem i = sp.get("IBM");
        System.out.println("IBM:" + i);

        sp.remove("SAP");

        System.out.println("----- List of stock items -----");
        ArrayList<String> codes = sp.getAllItemCodes();
        for (String n : codes) {
            i = sp.get(n);
            System.out.println(n + ": " + i);
        }
    }

}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the HashMap and ArrayList collection classes | imitation task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the HashMap and ArrayList classes

#### Learning Activities

1) read the given Java code
2) run the program
3) design and implement the requested StockPortfolio class
4) run and test the StockPortfolio class

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5  
[tutorialspoint.com: Java - HashMap](https://www.tutorialspoint.com/java/util/java_util_hashmap.htm)  
[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0

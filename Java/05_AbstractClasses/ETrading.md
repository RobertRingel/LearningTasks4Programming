Topic: abstract classes

## Learning Task: E-Trading

Develop and implement an e-Trading demo application that provides services to sell and buy items for registered buyers and sellers. The bases of this Java programm shall be an abstract class that defines the essential trading services - such as:  
- buy an item for a dedicated price as a named buyer  
- sell an item for a certain price as a named seller  
- register as a named buyer  
- register as a named seller

The items to be traded here are modelled  in the [TradeObject-class](TradeObject.java). The ETrading class will store these TradeObject instances by their names. The class will implement the trading services defined by the abstract class. And it would be benefitial if it could print a list of all sold items upon request.

 

---------------------------------------

### Solution

**An example of the abstract class: AbstractTradingService**

``` java
package org.htwd.pool.o5;

public abstract class AbstractTradingService {

    public AbstractTradingService() {}
    abstract public boolean buyItem(String item, double price, String buyerID);
    abstract public boolean sellItem(String item, double price, String sellerID);
    abstract public boolean registerBuyer(String name);
    abstract public boolean registerSeller(String name);
}
``` 

**An example ot the ETrading class**
``` java
package org.htwd.pool.o5;

import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;

public class ETrading extends AbstractTradingService {

    ArrayList<String> buyers = new ArrayList<String>();
    ArrayList<String> sellers = new ArrayList<String>();
    HashMap<String, TradeObject> tradePool = new HashMap<String, TradeObject>();
    ArrayList<String> soldObjects = new ArrayList<String>();

    public ETrading() { }

    @Override
    public boolean buyItem(String item, double price, String buyerID) {
        if (buyers.contains(buyerID) == false)
            return false;
        TradeObject t = tradePool.get(item);
        if (t == null)
            return false;
        if (t.getPrice() > price)
            return false;
        t.setPrice(price);
        t.setBuyer(buyerID);
        LocalTime locTime = LocalTime.now();
        String sold = locTime.toString() + " " + t.toString();
        soldObjects.add(sold);
        tradePool.remove(item);
        return true;
    }

    @Override
    public boolean sellItem(String item, double price, String sellerID) {
        if (sellers.contains(sellerID) == false)
            return false;
        TradeObject t = tradePool.get(item);
        if (t != null)
            return false; // item already in pool
        if (price < 0.0)
            return false;
        t = new TradeObject(item, price, sellerID);
        tradePool.put(item, t);
        return true;
    }

    @Override
    public boolean registerBuyer(String name) {
        if (buyers.contains(name))
            return false;
        buyers.add(name);
        return true;
    }

    @Override
    public boolean registerSeller(String name) {
        if (sellers.contains(name))
            return false;
        sellers.add(name);
        return true;
    }

    public void printSoldObjects() {
        for (String str : soldObjects )
            System.out.println(str);
    }

    public static void main(String[] args) {
        ETrading et = new ETrading();
        et.registerBuyer("Max");
        et.registerSeller("Liz");
        et.sellItem("Gift Box", 4.12, "Liz");
        et.sellItem("Sun glass", 14.09, "Liz");
        et.buyItem("Gift Box", 5.05, "Max");
        et.printSoldObjects();
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise abstract classes design and application | conventional task  | 2 - normal  | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
col-1: basics of the HashMap and ArrayList classes  
abs-1: basics of abstract classes

#### Learning Activities

1) read the code of the TradeObject class  
2) design the abstract class for the trading services    
3) design and implement the eTrading-class  
4) implement a main-method to test and demonstrate the eTrading-functionality  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

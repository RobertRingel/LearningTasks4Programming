Topic: classes, modifiers

## Learning Task: Voucher for beverages

Implement a Java class for voucher of your own to be used for buying beverages like soft drinks, beer or wine. Technically, the class might be similar to the Account class and the Voucher class.

---------------------------------------

### Solution

The solution should be a basic Java class. Focus is on basic class features like attribute, methods and modifiers.

The following Java program shows a potential demo solution as inspiration.

``` java
package org.htwd.pool.o1;

public class VoucherBeverages {
    static protected final double DEFAULT_VALUE = 50.0;
    static protected final double PRICE_SOFTDRINK = 2.0;
    static protected final double PRICE_BEER = 3.0;
    static protected final double PRICE_WINE = 5.0;

    private final String ID;
    private double currentValue;

    public VoucherBeverages(String id) {
        this.ID = id;
        this.currentValue = VoucherBeverages.DEFAULT_VALUE;
    }

    public boolean buySoftDrink() {
        if (this.currentValue < VoucherBeverages.PRICE_SOFTDRINK)
            return false;
        this.currentValue = this.currentValue - VoucherBeverages.PRICE_SOFTDRINK;
        return true;
    }

    public boolean buyBeer() {
        if (this.currentValue < VoucherBeverages.PRICE_BEER)
            return false;
        this.currentValue = this.currentValue - VoucherBeverages.PRICE_BEER;
        return true;
    }

    public boolean buyWine() {
        if (this.currentValue < VoucherBeverages.PRICE_WINE)
            return false;
        this.currentValue = this.currentValue - VoucherBeverages.PRICE_WINE;
        return true;
    }

    public double getCurrentValue() {
        return this.currentValue;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.ID);
        sb.append(" : ");
        sb.append(this.currentValue);
        sb.append(" EUR");
        return sb.toString();
    }

    public static void main(String args[]) {
        VoucherBeverages v = new VoucherBeverages("abc123");
        v.buyBeer();
        v.buySoftDrink();
        v.buyWine();
        System.out.println(v);
        System.out.println("Current value [EUR]:" + v.getCurrentValue());
    }
}
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| implementation of a basic class using appropriate modifiers | imitation task | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) read the task and understand it
2) develop an idea of the new Java class
3) implement the Java class
4) run the code and test it

#### Supporting information

[Account class](AccountClass.md) and [Voucher class](Voucher.md)  

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 134-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

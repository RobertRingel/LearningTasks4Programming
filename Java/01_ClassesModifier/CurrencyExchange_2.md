Topic: classes, modifiers

## Learning Task: Java class to model currency exchange

Implement a Java class to model currency exchange. The class shall be dedicated to a pair of a home currency and a foreign currency. It shall hold a price for buying the foreign currency and a price for selling it. These two prices shall be updated by appropriate methods. A toString-method is also required as well as a main-method to demonstrate the features of this class.

Compare your implementation with another student and may be with the sample solution.

---------------------------------------

### Solution

``` java
package org.htwd.pool.o1;

public class CurrencyExchange {

    private final String homeCurrency;
    private final String foreignCurrency;
    private double buyRate;
    private double sellRate;

    public CurrencyExchange(String home, String foreign, double buy, double sell) {
        this.homeCurrency = home;
        this.foreignCurrency = foreign;
        this.buyRate = buy;
        this.sellRate = sell;
    }

    public double buyForeign(double amount) {
        return this.buyRate * amount;
    }

    public double sellForeign(double amount) {
        return this.sellRate * amount;
    }

    public boolean setBuyRate(double r) {
        if (r <= 0.0)
            return false;
        this.buyRate = r;
        return true;
    }

    public boolean setSellRate(double r) {
        if (r <= 0.0)
            return false;
        this.sellRate = r;
        return true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.homeCurrency);
        sb.append(" > ");
        sb.append(this.foreignCurrency);
        sb.append(": buy: ");
        sb.append(this.buyRate);
        sb.append(": sell: ");
        sb.append(this.sellRate);
        return sb.toString();
    }

    public static void main(String[] args) {
        CurrencyExchange ce = new CurrencyExchange("EUR", "YEN", 174.05, 173.00);
        double val = ce.buyForeign(100.00);
        val = ce.sellForeign(100.00);
        ce.setBuyRate(174.99);
        ce.setSellRate(174.19);
        System.out.println(ce);
    }
}
```

| **Learning objective**                         | **Task type**     | **Complexity** |
| ---------------------------------------------- | ----------------- | -------------- |
| design, implement, test a basic Java class     | conventional task | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) get an understanding of the problem
2) identify class attributes and class methods
3) implement the class including main-mathod
4) run and test the program
5) compare the solution with another student and may be with the sample solution

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

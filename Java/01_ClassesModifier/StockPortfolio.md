Topic: classes, modifiers

## Learning Task: Java class to model a stock portfolio

Implement a Java class to serve as the bases of a stock portfolio. The class StockPortfolioItem shall store the required data for a stock item. This includes the ID of the stock item, the current stock price, the number of pieces hold in the portfolio item as well as the average price of all the items have been bought at. The class should provide methods to buy and sell stock items, to update the stock price, to calculate the current value of the StockPortfolioItem and to get a string information of all the class data.  
Implement a main-method to demonstrate the class usage.

Compare your implementation with an other student and may be with the sample solution.

---------------------------------------

### Solution

``` java
package org.htwd.pool.o1;

public class StockPortfolioItem {
    final String StockID;
    double Pieces;
    double avgPrice;
    double StockPrice;

    public StockPortfolioItem(String stock) {
        this.StockID = stock;
        this.Pieces = 0.0;
        this.avgPrice = 0.0;
        this.StockPrice = 0.0;
    }

    public void setStockPrice(double price) {
        if (price > 0.0)
            this.StockPrice = price;
    }

    void buy(double pcs, double price) {
        this.avgPrice = (this.Pieces/(this.Pieces+pcs))*this.avgPrice + (pcs/(this.Pieces+pcs))*price;
        this.Pieces += pcs;
    }

    double sell(double pcs, double price) {
        if (pcs < this.Pieces) {
            this.Pieces = this.Pieces - pcs;
            return pcs * price;
        }
        return 0.0;
    }

    double getValue() {
        return this.Pieces * this.StockPrice;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.StockID);
        sb.append(" : Pieces: ");
        sb.append(this.Pieces);
        sb.append(" avg buy price: ");
        sb.append(this.avgPrice);
        sb.append(" curr. stock price: ");
        sb.append(this.StockPrice);
        sb.append(" curr. value: ");
        sb.append(getValue());
        return sb.toString();
    }

    public static void main(String[] args) {
        StockPortfolioItem p = new StockPortfolioItem("IBM");
        p.buy(10,238.12);
        p.buy(10,239.12);
        p.setStockPrice(241.50);
        System.out.println(p);
        double v = p.sell(5,240.00);
        System.out.println(p);
    }
}
```

| **Learning objective**                         | **Task type**     | **Complexity** |
| ---------------------------------------------- | ----------------- | -------------- |
| classes encapsulate data, modifiers control access | conventional task | 1 - low       |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) get an understanding of the problem
2) identify class attributes and class methods
3) implement the class including main-mathod
4) run and test the program
5) compare the solution with an other student and may be with the sample solution

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0
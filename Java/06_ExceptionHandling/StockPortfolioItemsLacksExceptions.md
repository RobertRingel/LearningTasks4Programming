Topic: exception handling

## Learning Task: This class lacks exceptions

The StockPortfolioItem-class can be used to buy and sell stock items. The class is ready to run. However its code is not safe regarding invalid method call parameters. Read the code and run it in order to identify these weaknesses.  
Improve the implementation by throwing unchecked exceptions in case the methods are called by invalid parameter values. Test your implementation by appropriate main-methods calls to the related methods of the StockPortfolioItem-class.

``` java
package org.htwd.pool.o6;

public class StockPortfolioItem {
    final String stockID;
    double pieces;
    double avgPrice;
    double stockPrice;

    public StockPortfolioItem(String stock) {
        this.stockID = stock;  
        this.pieces = 0.0;
        this.avgPrice = 0.0;
        this.stockPrice = 0.0;
    }

    public void setStockPrice(double price)  {
        if (price > 0.0)    
            this.stockPrice = price;
    }

    void buy(double pcs, double price) {
        this.avgPrice = (this.pieces/(this.pieces+pcs))*this.avgPrice + (pcs/(this.pieces+pcs))*price;
        this.pieces += pcs;
    }

    double sell(double pcs, double price) {
        if (pcs < this.pieces) {
            this.pieces = this.pieces - pcs;
            return pcs * price;
        }
        return 0.0;
    }

    double getValue() {
        return this.pieces * this.stockPrice;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.stockID);
        sb.append(" : Pieces: ");
        sb.append(this.pieces);
        sb.append(" avg buy price: ");
        sb.append(this.avgPrice);
        sb.append(" curr. stock price: ");
        sb.append(this.stockPrice);
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

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

public class StockPortfolioItem {
    final String stockID;
    double pieces;
    double avgPrice;
    double stockPrice;

    public StockPortfolioItem(String stock) {
        if (stock==null || stock=="")
            throw new IllegalArgumentException("stock variable value is undefined!");
        this.stockID = stock;  
        this.pieces = 0.0;
        this.avgPrice = 0.0;
        this.stockPrice = 0.0;
    }

    public void setStockPrice(double price)  {
        if (price > 0.0)    
            this.stockPrice = price;
        else
            throw new IllegalArgumentException("stock price is negative!");
    }

    void buy(double pcs, double price) {
        if (pcs<0.0)
            throw new IllegalArgumentException("pcs must be greater than zero!");
        if (price<0.0)
            throw new IllegalArgumentException("price must be greater than zero!");
        this.avgPrice = (this.pieces/(this.pieces+pcs))*this.avgPrice + (pcs/(this.pieces+pcs))*price;
        this.pieces += pcs;
    }

    double sell(double pcs, double price) {
        if (pcs<0.0)
            throw new IllegalArgumentException("pcs must be greater than zero!");
        if (price<0.0)
            throw new IllegalArgumentException("price must be greater than zero!");
        if (pcs < this.pieces) {
            this.pieces = this.pieces - pcs;
            return pcs * price;
        }
        return 0.0;
    }

    double getValue() {
        return this.pieces * this.stockPrice;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.stockID);
        sb.append(" : Pieces: ");
        sb.append(this.pieces);
        sb.append(" avg buy price: ");
        sb.append(this.avgPrice);
        sb.append(" curr. stock price: ");
        sb.append(this.stockPrice);
        sb.append(" curr. value: ");
        sb.append(getValue());
        return sb.toString();
    }

    public static void main(String[] args) {
        StockPortfolioItem p = new StockPortfolioItem(null);
        p.buy(10,238.12);
        p.buy(-10,239.12);
        p.setStockPrice(241.50);
        System.out.println(p);
        double v = p.sell(5,-240.00);
        System.out.println(p);
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| apply exception handling                         | completion task | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling

#### Learning Activities

1) read and run the given Java code
2) identify potential invalid method parameter values  
3) fix these problems by throwing appropriate exceptions   
4) test the new implementation by calling these methods from the main-method

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 6, pages 187-204

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

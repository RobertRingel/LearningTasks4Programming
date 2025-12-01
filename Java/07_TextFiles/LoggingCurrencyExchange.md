Topic: text files

## Learning Task: Logging currency exchange

The given Java class can be used to perform currency exchange calculations. Read and run the code in order to understand it.  
Extend the code in a way to log any buy and sell activity into a text file. The extension shall be implemented as a new class that extends the given CurrencyExchange-class.  
Test your implementation with help of an appropriate main-method. Finally compare your code to the given sample solution.

``` java
package org.htwd.pool.o7;

public class CurrencyExchange {

    private final String HomeCurrency;
    private final String ForeignCurrency;
    protected double BuyRate;
    protected double SellRate;

    public CurrencyExchange(String home, String foreign, double buy, double sell) {
        this.HomeCurrency = home;
        this.ForeignCurrency = foreign;
        this.BuyRate = buy;
        this.SellRate = sell;
    }

    public double buyForeign(double amount) {
        return this.BuyRate * amount;
    }

    public double sellForeign(double amount) {
        return this.SellRate * amount;
    }

    public boolean setBuyRate(double r) {
        if (r <= 0.0)
            return false;
        this.BuyRate = r;
        return true;
    }

    public boolean setSellRate(double r) {
        if (r <= 0.0)
            return false;
        this.SellRate = r;
        return true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.HomeCurrency);
        sb.append(" > ");
        sb.append(this.ForeignCurrency);
        sb.append(": buy: ");
        sb.append(this.BuyRate);
        sb.append(": sell: ");
        sb.append(this.SellRate);
        return sb.toString();
    }

    public static void main(String[] args) {
        CurrencyExchange ce = new CurrencyExchange("EUR", "YEN", 174.05, 173.00);
        ce.buyForeign(100.00);
        ce.sellForeign(100.00);
        ce.setBuyRate(174.99);
        ce.setSellRate(174.19);
        System.out.println(ce);
    }
}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o7;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class LoggedCurrencyExchange extends CurrencyExchange {

    private final String DEFAULT_LOGFILENAME = "Log4CurrencyExchange.log";
    private String filename = DEFAULT_LOGFILENAME;

    public LoggedCurrencyExchange(String home, String foreign, double buy, double sell, String fileName) {
        super(home, foreign, buy, sell);
        if (fileName != null)
            this.filename = fileName;
        new File(this.filename);
    }

    public double buyForeign(double amount) {
        try {
            FileWriter writer = new FileWriter(this.filename, true);
            writer.write(super.toString() + "\t buy: " + amount + "\n");
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing log file: "+e.getMessage());
        }
        return super.BuyRate * amount;
    }

    public double sellForeign(double amount) {
        try {
            FileWriter writer = new FileWriter(this.filename, true);
            writer.write(super.toString() + "\t sell:" + amount + "\n");
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing log file: "+e.getMessage());
        }
        return super.SellRate * amount;
    }

    public static void main(String[] args) {
        LoggedCurrencyExchange ce = new LoggedCurrencyExchange("EUR", "YEN", 174.05, 173.00, null);
        ce.buyForeign(100.00);
        ce.sellForeign(80.00);
        ce.setBuyRate(174.99);
        ce.setSellRate(174.19);
        System.out.println(ce);
    }
}
```


| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file writing in problem solving       | completion task   | 2 - normal     |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
exc-1: basics of exception-handling  
txt-1: basics of text file writing  

#### Learning Activities

1) read and run the given Java program  
2) implement an extension of the given class  
3) implement the relevant text file writing methods  
4) test the new class using an appropriate main-method  
5) compare the new implementation to the given sample solution

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: Chapter 10, pages 311-329

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

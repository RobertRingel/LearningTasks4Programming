Topic: classes, modifiers

## Learning Task: Currency exchange calculation

Develop a Java class that provides a service to calculate currency exchanges from one currency to another one based on an exchange rate.

Implement the class and test it with help of a main-method.

---------------------------------------

### Solution

The basic idea to solve this task is:  
**Class name:**  
CurrencyExchange  

**attributes:**   
String: fromCurreny e.g. EUR  
String: toCurreny e.g. YEN  
double: rate e.g. 164.05  

**methods:**   
constructor: CurrencyExchange(String from, String to, double rate)  
setRate(double rate) ... to update the exchange rate   
double exchange(double amount) ... to calculate an exchange  
String toString() ... to get a String representation of the class

``` java
package org.htwd.pool.o1;

public class CurrencyExchange {

    private String fromCurrency;
    private String toCurrency;
    private double rate = -1.0;

    public CurrencyExchange(String from, String to, double rate) {
        this.fromCurrency = from;
        this.toCurrency = to;
        this.setRate(rate);
    }

    public void setRate(double rate) {
        if (rate > 0.0)
            this.rate = rate;
        else
            System.out.println("Illegal rate: "+rate);
    }

    public double exchange(double amount) {
        if (amount > 0.0) {
            double ex_amount = amount * this.rate;
            System.out.println("Exchange of "+amount+ " "+ this.fromCurrency+" yields "+ ex_amount+" "+this.toCurrency);
            return ex_amount;
        }
        System.out.println("Negative amount - no exchange!");
        return 0.0;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.fromCurrency);
        sb.append(" > ");
        sb.append(this.toCurrency);
        sb.append(" : ");
        sb.append(this.rate);
        return sb.toString();
    }

    public static void main(String[] args) {
        CurrencyExchange ce = new CurrencyExchange("EUR", "YEN", 171.64);
        ce.exchange(10.0);
        ce.exchange(-100.0);
        ce.setRate(-170.01);
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

1) understand the task
2) develop an idea to solve the task - identify class name, attributes, methods
3) implement the class in Java code
4) implement the main-method to test the class
5) run the code and test it

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 134-156

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

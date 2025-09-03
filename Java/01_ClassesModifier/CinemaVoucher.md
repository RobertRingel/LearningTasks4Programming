Topic: classes, modifiers

## Learning Task: Cinema voucher

Implement a basic class to model a cinema voucher similar to the BeaveragesVoucher class.

Implement your code, run it, test it and explain it to another student.

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

---------------------------------------

### Solution

The sample solution shown here is very similar to the class "VoucherBeverages". However the CinemaVoucher sample has no attribute "id". But it implements a class attribute to name the company that issues the voucher.

``` java
package org.htwd.pool.o1;

public class CinemaVoucher {
    public static final String COMPANY = "Cinemas United International Ltd.";
    private double value;

    public static final double SPECIAL_PRICE = 5.0;
    public static final double STD_SEAT_PRICE = 7.0;

    public CinemaVoucher(double value){
        this.value = value;
    }

    public double getValue() {
        return this.value;
    }

    public void paySpecialPrice() {
        if (this.value >= CinemaVoucher.SPECIAL_PRICE)
            this.value = this.value - CinemaVoucher.SPECIAL_PRICE;
        else {
            System.out.println("There is not enough money on the voucher");
            System.out.println(this.toString());
        }
    }

    public void payStandardPrice() {
        if (this.value >= CinemaVoucher.STD_SEAT_PRICE)
            this.value = this.value - CinemaVoucher.STD_SEAT_PRICE;
        else {
            System.out.println("There is not enough money on the voucher");
            System.out.println(this.toString());
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(CinemaVoucher.COMPANY);
        sb.append(" : ");
        sb.append(this.value);
        sb.append(" EUR");
        return sb.toString();
    }

    public static void main(String args[]) {
        CinemaVoucher v = new CinemaVoucher(50.0);
        v.payStandardPrice();
        System.out.println(v);
    }
}
```

| **Learning objective**                         | **Task type**     | **Complexity** |
| ---------------------------------------------- | ----------------- | -------------- |
| classes encapsulate data, modifiers control access | imitation task | 1 - low       |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) get an understanding of the problem
2) get an idea for the adaptation towards a similar cinema voucher
3) implement the program
4) run and test the new program
5) compare the solution with another student

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

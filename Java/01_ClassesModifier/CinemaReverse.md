Topic: classes, modifiers

## Learning Task: Reverse Task "Cinema"

Read, analyse and run the given Java program. What is it's purpose?
Write the text for a related programming task.

``` java
package org.htwd.pool.o1;

public class CinemaVoucher {
    public static final String COMPANY = "Cinemas United Internation Ltd.";
    private double Value;

    public static final double SPECIAL_PRICE = 5.0;
    public static final double STD_SEAT_PRICE = 7.0;

    public CinemaVoucher(double value){
        this.Value = value;
    }

    public double getValue() {
        return this.Value;
    }

    public void paySpecialPrice() {
        if (this.Value >= CinemaVoucher.SPECIAL_PRICE)
            this.Value = this.Value - CinemaVoucher.SPECIAL_PRICE;
        else {
            System.out.println("There is not enough money on the voucher");
            System.out.println(this.toString());
        }
    }

    public void payStandardPrice() {
        if (this.Value >= CinemaVoucher.STD_SEAT_PRICE)
            this.Value = this.Value - CinemaVoucher.STD_SEAT_PRICE;
        else {
            System.out.println("There is not enough money on the voucher");
            System.out.println(this.toString());
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(CinemaVoucher.COMPANY);
        sb.append(" : ");
        sb.append(this.Value);
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

---------------------------------------

### Solution

This class models a very basic and straightforward cinema voucher.
The appropriate programming task might be formulated as:

Implemeent a Java class to model a basic cinema voucher. The primary attribute is the value of the voucher, that will be defined by the constructor. There shall be a class attribute to store the company name that issues these vouchers. The voucher shall be used to pay a  ticket for a standard seat price or a special price. It shall be possible to get the current remaining value of the voucher and to get a string information of the voucher.
Implement the appropriate methods and a main-method to demonstrate the class usage.

| **Learning objective**                         | **Task type**     | **Complexity** |
| ---------------------------------------------- | ----------------- | -------------- |
| classes encapsulate data, modifiers control access | reverse task  | 1 - low        |  

#### Previous Knowledge

bcm-1: basics of classes and modifiers  

#### Learning Activities

1) read and run the Java code
2) explain the purpose in a short and specific written statement
3) write a short and specific programming task, that yields the given Java program

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 1, 2

[tutorialspoint.com: Java - Classes and Objects](https://www.tutorialspoint.com/java/java_object_classes.htm)  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0
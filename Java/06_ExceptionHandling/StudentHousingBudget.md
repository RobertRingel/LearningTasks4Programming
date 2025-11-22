Topic: exception handling

## Learning Task: The student housing budget

Implement a Java program that can be used as a student housing budget calculator. The program shall get the overall monthly budget initially. Then it shall be possible to add different monthly budget items such as electricity, gas, water, food, donotions and the related monetary values to be stored in a HashMap. The program shall be able to print a budget overview and it shall be able to calculate the current saldo.  

When implementing this program make sure to store only valid budget items as well as a valid overall monthly initial budget value.

Demonstrate your result to another student.

---------------------------------------

### Solution

``` java
package org.htwd.pool.o6;

import java.util.HashMap;

public class StudentHousingBudget {

    private final double BUDGET;
    private HashMap<String,Double> budget = new HashMap<String, Double>();

    public StudentHousingBudget(double initial_budget) {
        if (initial_budget < 0.0)
            throw new IllegalArgumentException("initial budget can not be negative");
        this.BUDGET = initial_budget;
    }

    public void storeBudgetItem(String item, double value) {
        if (item == null || item == "")
            throw new IllegalArgumentException("item can not be empty");
        this.budget.put(item, Double.valueOf(value));
    }

    public void removeBudgetItem(String item) {
        if (item == null || item == "")
            throw new IllegalArgumentException("item can not be empty");
        this.budget.remove(item);
    }

    public void printOverview() {
        System.out.println(this.BUDGET + "\tINITIAL BUDGET");
        double value = 0.0;
        for (String k : this.budget.keySet()) {
            value = this.budget.get(k).doubleValue();
            System.out.println(value+"\t"+k);
        }
        double saldo = this.getSaldo();
        System.out.println(saldo + "\tSALDO");
        System.out.println((this.BUDGET+saldo)+"\tOUTCOME");
    }... any Java code similar to the sample implementation shown above.

    public double getSaldo() {
        double saldo = 0.0;
        for (String k : this.budget.keySet()) {
            saldo += this.budget.get(k).doubleValue();
        }
        return saldo;
    }

    public static void main(String[] args) {
        StudentHousingBudget shb = new StudentHousingBudget(500.0);
        shb.storeBudgetItem("electr. energy", -120.0);
        shb.storeBudgetItem("water supply", -40.0);
        shb.storeBudgetItem("rent price", -340.0);
        shb.printOverview();
    }
}
``` 

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply exception handling in problem solving      | conventional task | 2 - normal     | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
col-1: basics of the HashMap class  
exc-1: basics of exception-handling

#### Learning Activities

1) read and understand the given task  
2) design and implement the related class   
3) identify critical method parameters and validate them before storing - throw exceptions in case of invalid parameters   
4) demonstrate the final program to another student  

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 7  
[tutorialspoint.com: Java - Exceptions](https://www.tutorialspoint.com/java/java_exceptions.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

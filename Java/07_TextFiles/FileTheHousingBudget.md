Topic: text files

## Learning Task: File the housing budget

The following Java class is a program to setup student housing budgets. Read and run the program to obtain understanding.  

Your task is to add a method to store the budget into a text file of the following format:
 ``` java
500.0
-340.0:rent price
-120.0:electr. energy
-40.0:water supply
```
Then add a second method to read the budget from a text file into the program.

Test your program with help of an appropriate main-method. Compare your implementation with the given sample solution.

``` java
package org.htwd.pool.o7;

import java.io.*;
import java.util.HashMap;

public class StudentHousingBudget {

    private double BUDGET;
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
    }

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

---------------------------------------

### Solution

``` java
package org.htwd.pool.o7;

import java.io.*;
import java.util.HashMap;

public class StudentHousingBudget {
    ...
public void saveToFile(String fileName) {
        try {
            FileWriter writer = new FileWriter(fileName, false);
            writer.write(Double.toString(this.BUDGET)+"\n");
            for (String k:this.budget.keySet()) {
                writer.write(this.budget.get(k)+DELIMITER+k+"\n");
            }
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing log file: "+e.getMessage());
        }
    }

    public void loadFromFile(String fileName) {
        String line;
        this.budget.clear();
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            line = br.readLine();
            this.BUDGET = Double.parseDouble(line);
            while ((line = br.readLine()) != null) {
                String[] token = line.split(DELIMITER);
                if (token.length != 2)
                    throw new RuntimeException("corrupt line:"+line);
                String item = token[1].strip();
                double value = Double.parseDouble(token[0].strip());
                this.storeBudgetItem(item,value);
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found:"+fileName);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (RuntimeException e) {
            System.out.println("Error while reading a file:" + e.getMessage());
        }
    }

    public static void main(String[] args) {
        StudentHousingBudget shb = new StudentHousingBudget(500.0);
        shb.loadFromFile("budget0126.txt");
        shb.printOverview();
        shb.saveToFile("budget0126.txt");
    }
}
```

| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file reading and writing              | conventional task | 2 - normal     |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling  
txt-1: basics of text file reading and writing  

#### Learning Activities

1) read and run the given Java program  
2) implement a method to write the budget to a text file  
3) implement a method to read the budget from a text file  
4) test the implementation with help of an appropriate main-method  
5) compare the implementation to the sample solution  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
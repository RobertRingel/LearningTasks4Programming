Topic: text files

## Learning Task: Currency exchange rates

The following Java class CurrencyRates shall be used to perform various currency exchange calculations. It will load the currencies and their rates from the text file "ExchangeRates.txt". The file is structured as follows:  
``` java
EUR > YEN 174.05
EUR > USD 1.35
USD > GBP 1.02
```

Read the given Java program to understand its functionality and the related implementation.  
Implement the loadFromFile-method to support reading the above text file.
Finally test your implementation under various error cases - make sure your program can handle corrupt text file input lines.

``` java
package org.htwd.pool.o7;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class CurrencyRates {

    private HashMap<String, Double> rates = new HashMap<String, Double>();
    private final String FILENAME = "ExchangeRates.txt";

    public CurrencyRates() {
        this.loadFromFile();
    }

    private void loadFromFile() {
        // TODO: implement this method
    }

    public double exchange(String from, String to, double amount) {
        String k = from+">"+to;
        if (this.rates.containsKey(k)) {
            double rate = this.rates.get(k);
            return rate * amount;
        }
        System.out.println("ERROR: "+k+" is not supported.");
        return -1.0;
    }

    public String toString() {
        double r;
        StringBuilder sb = new StringBuilder("from>to : rate\n");
        for (String k : this.rates.keySet()) {
            r = this.rates.get(k);
            sb.append(k+" : "+r+"\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        CurrencyRates cr = new CurrencyRates();
        System.out.println(cr);
        double money = cr.exchange("EUR","YEN", 100.0);
        System.out.println(money);
    }
}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o7;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class CurrencyRates {

    private HashMap<String, Double> rates = new HashMap<String, Double>();
    private final String FILENAME = "ExchangeRates.txt";

    public CurrencyRates() {
        this.loadFromFile();
    }

   private void loadFromFile() {
        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                // EUR > YEN: 174.05
                String[] token = line.split(" ");
                if (token.length != 4)
                    throw new RuntimeException("corrupt line:" + line);
                String from = token[0];
                String to = token[2];
                double rate = Double.parseDouble(token[3]);
                String k = from + ">" + to;
                this.rates.put(k, Double.valueOf(rate));
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found:" + FILENAME);
        } catch (IOException e) {
            System.out.println("Error while reading file:" + FILENAME);
        } catch (RuntimeException e) {
            System.out.println("Error while reading a file:" + e.getMessage());
        }
    }

    ...

    public static void main(String[] args) {
        CurrencyRates cr = new CurrencyRates();
        System.out.println(cr);
        double money = cr.exchange("EUR","YEN", 100.0);
        System.out.println(money);
    }
}
```


| **Learning objective**                           | **Task type**     | **Complexity** |
| ------------------------------------------------ | ----------------- | -------------- |
| apply text file reading in problem solving       | completion task   | 2 - normal     |

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exc-1: basics of exception-handling  
txt-1: basics of text file reading and writing  

#### Learning Activities

1) read the given Java program to obtain understanding related to the given text file  
2) implement the loadFromFile-method  
3) test your implementation in various error cases  

#### Supporting information

[tutorialspoint.com: Java - Files and I/O](https://www.tutorialspoint.com/java/java_files_io.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0

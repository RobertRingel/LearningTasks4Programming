Topic: storing objects in collections

## Learning Task: Lottery Guess

Implement a Java class that models a lottery guess. A lottery guess represents a certain set of numbers in a defined number range and a defined count of numbers. Each number in a lottery guess is unique (there are no double numbers)!

The class shall provide methods to:  
- add a number to the guess  
- check whether a certain number is already part of the guess  
- print the guess  
- count the number of common numbers compared to another guess (count number of hits)

Use an ArrayList to store the numbers of the guess.

Test your implementation with help of the given main-method.  
Compare your Java code with the one of another student.

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class LotteryGuess {
    ...
    public static void main(String[] args) {
        LotteryGuess guess = new LotteryGuess(1, 35,5);
        guess.addNumber(1);
        guess.addNumber(1);
        guess.addNumber(2);
        guess.addNumber(3);
        guess.addNumber(4);
        guess.addNumber(5);
        guess.addNumber(6);
        System.out.println(guess);
        System.out.println(guess.containsNumber(Integer.valueOf(3)));

        LotteryGuess numbers = new LotteryGuess(1, 35,5);
        numbers.addNumber(2);
        numbers.addNumber(10);
        numbers.addNumber(11);
        numbers.addNumber(12);
        numbers.addNumber(13);
        System.out.println(guess.countHits(numbers));
    }
}
---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class LotteryGuess {
    private final int COUNT;
    private final int MIN;
    private final int MAX;
    private ArrayList<Integer> numbers = new ArrayList<Integer>();

    public LotteryGuess(int min, int max, int count) {
        this.COUNT = count;
        this.MIN = min;
        this.MAX = max;
    }
    public boolean addNumber(int n) {
        if (numbers.size()>=this.COUNT)
            return false;
        if (n<this.MIN || n>this.MAX)
            return false;
        Integer i = Integer.valueOf(n);
        if (numbers.contains(i))
            return false;
        numbers.add(i);
        return true;
    }

    public boolean containsNumber(Integer i) {
        return numbers.contains(i);
    }

    public int countHits(LotteryGuess other) {
        int hits = 0;
        for (Integer i:numbers) {
            if (other.containsNumber(i))
                hits++;
        }
        return hits;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (Integer i:numbers) {
            sb.append(i);
            sb.append(" : ");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        LotteryGuess guess = new LotteryGuess(1, 35,5);
        guess.addNumber(1);
        guess.addNumber(1);
        guess.addNumber(2);
        guess.addNumber(3);
        guess.addNumber(4);
        guess.addNumber(5);
        guess.addNumber(6);
        System.out.println(guess);
        System.out.println(guess.containsNumber(Integer.valueOf(3)));

        LotteryGuess numbers = new LotteryGuess(1, 35,5);
        numbers.addNumber(2);
        numbers.addNumber(10);
        numbers.addNumber(11);
        numbers.addNumber(12);
        numbers.addNumber(13);
        System.out.println(guess.countHits(numbers));
    }
}
```
| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the ArrayList collection classes | conventional task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the ArrayList class

#### Learning Activities

1) understand the requested features of the task
2) design and implement the class
3) run and test the implementation baseds on an appropriate main-method
4) compare the program with the solution of another student

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5  
[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0

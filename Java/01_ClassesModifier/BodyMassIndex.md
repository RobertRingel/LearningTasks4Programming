Topic: classes, modifiers

## Learning Task: Calculate the Body-Mass-Index

Write a Java program to ...

The ....

---------------------------------------

### Solution

``` java
package org.htwd;

public class Can extends Flask implements Refundable {

    private boolean returned = false;

    public Can(double refund) {
        super(refund);
    }

    @Override
    public double returnIt() {
        if (returned)
            return 0.0;
        returned = true;
        return getRefund();
    }

}
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding variables, calculation and result printing | conventional task | 1 - low |  

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: input statement, type-conversion function for int and float  

#### Learning Activities

1) understand the task
2) implement Python code for the calculation including result print-out
3) run the Python code and check the result


#### Supporting information

[tutorialspoint.com: ...](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: ...](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  



---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2025            
License: CC BY-SA 4.0

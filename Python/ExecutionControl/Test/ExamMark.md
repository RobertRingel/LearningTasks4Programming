### Learning Task: Exam Mark Calculation

The following program calculates the exam mark.  

Complete the code to calculate all exam marks according to the given limits:

Mark 1: score ratio >95%  
Mark 2: score ratio >80%   
Mark 3: score ratio >65%  
Mark 4: score ratio >=50%  
Mark 5: score ratio <50%

``` python
scr_ratio = int(input('Exam Score Ratio [%]:'))
mark = 5
if scr_ratio > 95:
    mark=1
elif scr_ratio > 80:
    mark=2

print('Exam mark:',mark)
```

---------------------------------------
---------------------------------------

##### Solution

``` python
scr_ratio = int(input('Exam Score Ratio [%]:'))
mark = 5
if scr_ratio > 95:
    mark=1
elif scr_ratio > 80:
    mark=2
elif scr_ratio > 65:
    mark=3
elif scr_ratio >= 50:
    mark=4

print('Exam mark:',mark)
```

##### Previous Knowledge

- print, input, variable
- if-elif-statement
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) extent the code by using elif-statements
4) run and test the final program


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Test and branch using if-elif"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: complition task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

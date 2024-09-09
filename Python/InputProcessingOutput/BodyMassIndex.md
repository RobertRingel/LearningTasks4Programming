### Learning Task: Calculate the Body-Mass-Index

Write a Python program to calculate the body-mass-index based on the user input for weight in kilogramms and body height in meters.
The related calculation equiation is bmi = mass / height²  

The body-mass-index of a healthy person with an age above 18 years should be in the range 18...25.

---------------------------------------
---------------------------------------

##### Solution

``` python
# Calculation of the body-mass-index

weight = int(input('Your weight [kg]:'))
height = float(input('Your height [m]:'))

bmi = weight/height**2

print('Your bmi:',bmi)
```

##### Previous Knowledge

- print and input statements
- variables and assignments to variables
- type-conversion function for int and float

##### Learning Activities

1) understand the task
2) implement Python code for the calculation including result print-out
3) run the Python code and check the result


###### Supporting information

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  

Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 



Seiten im THEIß-Buch  
[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)
[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)
----
[//]: # "Learning objective: Understanding of variables, calculation and result printing"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: conventional task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

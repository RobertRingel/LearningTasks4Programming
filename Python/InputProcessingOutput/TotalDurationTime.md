### Learning Task: Total time duration

Write a Python program to calculate the total duration time for the number of seconds given by user input.
The result shall be printed as hours:minutes:seconds.

---------------------------------------
---------------------------------------

##### Solution

``` python
# Calculation of a total duration in hours:minutes:seconds

duration_sec = int(input('Total duration in seconds:'))
hh = duration_sec//3600
rem_sec = duration_sec - hh*3600
mm = rem_sec//60
ss = rem_sec - mm*60
print('Total duration time (hours:minutes:seconds):',hh,':',mm,':',ss)
```

##### Previous Knowledge

- print and input statements
- variables and assignments to variables
- int-type-conversion function

##### Learning Activities

1) understand the task
2) decide for the propper calculation equiation using floor division
3) implement Python code for the calculation including result print-out
4) run the Python code and check the result


###### Supporting information

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 

----
[//]: # "Learning objective: Understanding of variables, calculation and result printing"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: conventional task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

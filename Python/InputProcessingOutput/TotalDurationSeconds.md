### Learning Task: Basic calculation

Write a Python program to calculate the total time duration in seconds, based on the user input of hours, minutes and seconds.

---------------------------------------
---------------------------------------

##### Solution

``` python
# Calculation of a total duration in seconds

hours = int(input('Number of hours:'))
minutes = int(input('Number of minutes:'))
seconds = int(input('Number of seconds:'))

duration_sec = hours*3600 + minutes*60 + seconds
print('Total duration in seconds:',duration_sec)
```

##### Previous Knowledge

- print and input statements
- variables and assignments to variables
- int-type-conversion function

##### Learning Activities

1) understand the task
2) decide for the propper calculation equiation
3) implement Python code for the calculation including result print-out
4) run the Python code and check the result


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)

----
[//]: # "Learning objective: Understanding of variables, calculation and result printing"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: conventional task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

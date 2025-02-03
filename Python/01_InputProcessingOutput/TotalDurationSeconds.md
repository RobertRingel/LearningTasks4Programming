Topic: variables, calculations, printing

## Learning Task: Total time duration in seconds

Write a Python program to calculate the total time duration in seconds, based on the user input of hours, minutes and seconds.

---------------------------------------

### Solution

``` python
# Calculation of a total duration in seconds

hours = int(input('Number of hours:'))
minutes = int(input('Number of minutes:'))
seconds = int(input('Number of seconds:'))

duration_sec = hours*3600 + minutes*60 + seconds
print('Total duration in seconds:',duration_sec)
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding of variables, calculation and result printing | conventional task | 1 - low     |  

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: input statement, int-type-conversion function

#### Learning Activities

1) understand the task
2) decide for the propper calculation equiation
3) implement Python code for the calculation including result print-out
4) run the Python code and check the result

#### Supporting information

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:
Kapitel 2, Seiten 23-27 und Kapitel 3, Seiten 37-39

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
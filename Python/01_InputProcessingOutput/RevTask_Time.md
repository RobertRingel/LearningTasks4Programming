Topic: variables, calculations, printing

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
duration_sec = int(input('Total duration in seconds:'))
hh = duration_sec//3600
rem_sec = duration_sec - hh*3600
mm = rem_sec//60
ss = rem_sec - mm*60
print('Total duration time (hours:minutes:seconds):',hh,':',mm,':',ss)
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the total duration time for the number of seconds given by user input.

*Programming task*  
Write a Python program to calculate the total duration time for the number of seconds given by user input.
The result shall be printed as hours:minutes:seconds.

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding of variables, calculation and result printing | reverse task | 1 - low |  

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: int-type-conversion function

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T.  (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:
Kapitel 2, Seiten 23-27 und Kapitel 3, Seiten 37-39

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
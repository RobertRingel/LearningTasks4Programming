Topic: controlling program execution - loop

## Learning Task: Monthly balance over the year

Implement a program to calculate the monthly balance of an account over the year.  
The program will run for 12 months and the user will enter the monthly earnings and the monthly expanses. 
The program will cumulate these values in order to print the outcome per year after 12 months.

Demonstrate your program to an other student and explain it!

---------------------------------------

### Solution

``` python
# Monthly Balance over the year

total = 0.0      # cumulated total outcome
month = 0        # month number

while month < 12:                              # run for 12 months
	month = month +1                           # increment the month counter
	print('Month:',month)
	earn = float(input('Earnings [EUR]: '))
	exp = float(input('Expenses [EUR]: '))
	total = total + earn - exp                 # update the cumulated total

print('Outcome per year [EUR]:', total)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections                   | conventional task | 1 - low      |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
loop-1: while-loop  

#### Learning Activities

1) read the task and discuss the problem
2) write appropriate Python code
3) test the Python program
4) speek about your code with another student - add comments to the code

#### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 7, pages 118-121

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 60-62

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

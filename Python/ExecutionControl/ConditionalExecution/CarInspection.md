### Learning Task: Car Maintenance

The following Python code gives recommendations regarding potential car maintenance.  

Read the code and and run the code. Test and challenge the code. Do see any problems?  
Name these problems and try to fix them.

``` python
INSPECTION_LIMIT = 30
MILE_LIMIT = 20000

months = int(input('Months since last vehicle inspection:'))
milage = int(input('Miles since last oil change:'))

if months>INSPECTION_LIMIT:
	print('recommended vehicle inspection!')
elif milage>MILE_LIMIT:
	print('recommended oli change!')
else:
	print('no action required.')
```

---------------------------------------
---------------------------------------

##### Solution

The above code will process negative numbers in the user input.
In case the inspection limit is overdue, it will not check the milage limit.  
The code below fixes these problems.

``` python
INSPECTION_LIMIT = 30
MILE_LIMIT = 20000

months = int(input('Months since last vehicle inspection:'))
milage = int(input('Miles since last oil change:'))

ok = True
valid = months>0 and milage>0

if valid and months>INSPECTION_LIMIT:
	print('recommended vehicle inspection!')
	ok = False

if valid and milage>MILE_LIMIT:
	print('recommended oli change!')
	ok = False

if not valid:
	print('invalid input data')
elif ok:
	print('no action required.')
```

##### Previous Knowledge

- print, input, boolean variables
- if-elif-statement
  
##### Learning Activities

1) read and run the Python code
2) identify problems in the code
3) get an understanding of the code
4) develop ideas to fix the problems - note the ideas
5) implement the fixes
6) run the fixed code


###### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 

----
[//]: # "Learning objective: Test and branch using if-elif and boolean variables"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: completion task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

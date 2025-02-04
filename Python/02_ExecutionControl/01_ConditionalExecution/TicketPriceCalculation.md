Topic: controlling program execution - branch

## Learning Task: Ticket Price Calculation

Implement a ticket price calculation similar to the Cinema-Ticket-Price-Calculation.  
Make assumptions for ticket classes and related standard prices. Make assumptions for certain discounts. Get the ticket amounts for user input and perform the related price calculation. Do not forget to perform a check for valid user input.

Implement your code, run it, test it and explain it to another student.

``` python
# ticket price calculator

... the students code to be written here
```

---------------------------------------

### Solution

This is the example of the Cinema-Ticket-Price-Calculation

``` python
# Cinema ticket price calculator

KIDS_PRICE = 5.0
SEN_PRICE = 6.5
STD_PRICE = 9.0

kids = int(input('Number of kids tickets:'))
sen = int(input('Number of senior tickets:'))
std = int(input('Number of standard tickets:'))

valid = True
if kids<0 or sen<0 or std<0:
	valid = False

kids_rate = 1.0
std_rate = 1.0
if valid:
	if kids>4:
		kids_rate = 0.5
	if std>5:
		std_rate = 0.3
	price = kids*KIDS_PRICE*kids_rate + sen*SEN_PRICE + std*STD_PRICE*std_rate
	print('Your total ticket pric is EUR:', price)
else:
	print('Invalid input data.')
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| test and branch using if-else including conjunction | imitation task | 1 - low    |  

#### Previous Knowledge

vcp-1, vcp-2: print, variables and assignments to variables, type conversion for numeric input  
branch-2: if-else-statements

#### Learning Activities

1) get an understanding of the problem
2) get an idea for a similar real live problem
3) implement the program
4) run and test the new program
5) compare the solution with an other student

#### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 41-48

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
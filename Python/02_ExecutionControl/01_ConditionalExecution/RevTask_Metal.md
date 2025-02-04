Topic: controlling program execution - branch

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
# --- Prices per Gramm in Euro ---
GOLD_PRICE = 73.25          
SILVER_PRICE = 0.83         
PLATINUM_PRICE = 27.26

price = -1.0

metal = input('Metal (g=Gold, s=silver, p=platinum):')
mass = float(input('Mass [g]:'))

if metal == 'g':
	price = GOLD_PRICE
elif metal == 's':
	price = SILVER_PRICE
elif metal == 'p':
	price = PLATINUM_PRICE

if price > 0.0 and mass > 0.0:
	value = mass * price
	print('The value is [EUR]:',value)
else:
	print('Invalid input.')
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the monetary value for a given weight of Gold, Silver or Platinum.

*Programming task*  
Write a Python program to calculate the monetary value for a given weight of Gold, Silver or Platinum.
The user shall enter the  kind of metal and the related weight and the programm shall calculate the according value. In case of an invalid input the programm shall print a message. Otherwise it will perform the calculation and print the result.

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| test and branch using if-else including conjunction | reverse task | 1 - low      |  

#### Previous Knowledge

vcp-1, vcp-2: variables, calculations, print, type conversion for numeric input  
branch-2: if-elif-else-statements

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

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
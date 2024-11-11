### Learning Task: Factorial

The following program calculates the factorial using a recursive function call.

Read the code, run the programm and write comments to the code. Highlight the 
recursive function call inside the function implementation.

``` python
def factorial(n):
	"""
	Calculate the factorial using a recursive function call.

	Args:
		n (int) : the number to calculate the factorial

	Returns:
		int : the factorial
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# --- main part ---
num = 8
fac = factorial(num)
print('Factorial of', num, '=', fac)
```

---------------------------------------
---------------------------------------

##### Solution

``` python
def factorial(n):
	"""
	Calculate the factorial using a recursive function call.

	Args:
		n (int) : the number to calculate the factorial

	Returns:
		int : the factorial
	"""
	if n == 0:   # factorial of 0 is 1
		return 1
	else:   # calculate factorial for n-1 by recursive function call
		return n * factorial(n-1) 

# --- main part ---
num = 8
fac = factorial(num)
print('Factorial of', num, '=', fac)
```
##### Previous Knowledge

- basics of branches
- basics of functions
  
##### Learning Activities

1) read and run the given Python program
2) write comments to the code
3) identify the recursive function call

##### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Functions 

*Learning objective:*  
- understand recursive functions call 

[//]: # "learning objective: 3-function"
[//]: # "previous knowledge: 2-branch 1-function"

*Complexity:*  1-low 

*Task type:*  worked-out-example

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

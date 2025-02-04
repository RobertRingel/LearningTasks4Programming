Topic: controlling program execution - loop
## Learning Task: Arithmetic mean calculation

The following program shall calculate the arithmetic mean of the sequence of numbers entered by the user.

Read the program and write comments to significant lines in the code.  
Implement the missing statements to exit the loop, in case the users enters the number 0. Then run the programm and test it.

Add-on task: Adds some lines of code to print a message in case the user enters a negative number. 

``` python
# --- Calculation of the arithmetic mean ---

print('*** Calculate the average of numbers greater 0 ***')

i = 0
total = 0

while True:
	print('Enter Number >0 (0=end)')
	number = int(input('Number:'))
	if number>0:
		total = total + number
		i = i+1

avg = total/i
print('The average value is:',avg)

```

---------------------------------------

### Solution

``` python
# --- Calculation of the arithmetic mean ---

print('*** Calculate the average of numbers greater 0 ***')

i = 0                                  # number counter
total = 0                              # sum of entered numbers

while True:                            # infinite loop to process numbers
	print('Enter Number >0 (0=end)')
	number = int(input('Number:'))
	if number>0:			    # valid number?
		total = total + number      # yes:  sum up the numbers 
		i = i+1                     #       increment number counter
	elif number == 0:                   # number zero?
		break                       # yes:  exit the loop
	else:                               # --- add-on solution
		print('Invalid number!')    # --- add-on solution

mean = total/i                          # calculation of arithm. mean value
print('The arithmetic mean is:', mean)  # display the result
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections and break to exit a loop | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-elif-statement  
loop-2: while-loop including break-statement  
  
#### Learning Activities

1) read the Python code
2) get an understanding of the code
3) write comments to the code
4) implementation of test and break to exit the loop

#### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
[tutorialspoint.com: break-Statement](https://www.tutorialspoint.com/python/python_break_statement.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 7, pages 118-121

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 60-62

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
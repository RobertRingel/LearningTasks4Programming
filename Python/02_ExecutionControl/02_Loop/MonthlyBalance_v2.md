Topic: controlling program execution - loop

## Learning Task: Monthly balance over the year

The following Python program calculates the monthly balance of an account over the year.  

Improve the implementation in a way, to make sure that the input data for earnings and expenses is always a positive number!
In case one of them is negative, a warning message shall be shown and the data must be entered again, as long as it is not correct. 

Add the required Python commands, make comments to the new lines and test your implementation.  
Demonstrate your program to an other student and explain it!

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

### Solution

``` python
# Monthly Balance over the year

total = 0.0      # cumulated total outcome
month = 0        # month number

while month < 12:                              # run for 12 months
	month = month +1                               # increment the month counter
	print('Month:',month)
	while True:                                    # repeat until valid input
		earn = float(input('Earnings [EUR]: '))
		exp = float(input('Expenses [EUR]: '))
		if earn>=0.0 and exp>=0.0:             # valid input data?
			break                          # yes:  exit the loop
		else:                                  # no:
			print('Correct your input!')   #     print message
	total = total + earn - exp                     # update the cumulated total
	print(total)

print('Outcome per year [EUR]:', total)
``` 

***Help for students to get an idea about to code structure***
``` python
# Monthly Balance over the year

total = 0.0      # cumulated total outcome
month = 0        # month number

while month < 12:                              # run for 12 months
	month = month +1                               # increment the month counter
	print('Month:',month)
	while ...                                      # repeat until valid input
		earn = float(input('Earnings [EUR]: '))
		exp = float(input('Expenses [EUR]: '))
		if ...                   :             # valid input data?
			...                            # yes:  exit the loop
		else:                                  # no:
			...                            #     print message
	total = total + earn - exp                     # update the cumulated total
	print(total)

print('Outcome per year [EUR]:', total)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections, break a loop     | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-else-statement  
loop-2: while-loop including break-statement  

#### Learning Activities

1) read the task and discuss the problem
2) write appropriate Python code using a **nested infinite loop** and break
3) add comments to the code
4) test the Python program
5) speek about the code with another student

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

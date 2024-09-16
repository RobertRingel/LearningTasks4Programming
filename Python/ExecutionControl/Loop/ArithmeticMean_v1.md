### Learning Task: Arithmetic mean calculation

The following program shall calculate the arithmetic mean of the sequence of numbers entered by the user.

Read the program and write comments to significant lines in the code.  
Implement the missing two lines and then run the program to test it.
  

``` python
# --- Calculation of the arithmetic mean ---

n = int(input('How many values will be given?'))
i = 0
total = 0

while i<n:
	print('Enter Number',i+1)
	number = int(input('Number:'))
	total = total + number
	i = i+1

...                             # implement calculation of arithm. mean value
...                             # display the result

```

---------------------------------------
---------------------------------------

##### Solution

``` python
# --- Calculation of the arithmetic mean ---

n = int(input('How many values will be given?'))
i = 0                                    # number counter
total = 0                                # sum of entered numbers

while i<n:                               # loop to process all the numbers
	print('Enter Number',i+1)
	number = int(input('Number:'))
	total = total + number               # sum up all the numbers
	i = i+1                              # increment number counter

mean = total/n                           # calculation of arithm. mean value
print('The arithmetic mean is:', mean)   # display the result
```

##### Previous Knowledge

- print, input, variable
- while-loop
  
##### Learning Activities

1) read the Python code
2) get an understanding of the code
3) write comments to the code
4) implementation of calculation and print **outside the loop**


###### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 7, pages 118-121  

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 60-62 

----
[//]: # "Learning objective: Loop to repeat code sections"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: completion task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

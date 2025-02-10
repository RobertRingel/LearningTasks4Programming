Topic: controlling program execution - loop

## Learning Task: Minimum and maximum number

The following program determines the minimum and maximum number out of a random sequence of numbers.

Read the program, run it and write comments to the significant lines in the code.  
Finally explain your understanding of the program to another student.

``` python
mini = 9999999
maxi = -999999

print('Enter some numbers in the range 1 ... 1000')

while True:
	number = int(input('Number:'))
	if number<0 or number>1000:
		break
	if number < mini:
		mini = number
	elif number > maxi:
		maxi = number

print('The biggest number was:',maxi)
print('The smallest number was:',mini)
```

---------------------------------------

#### Solution

``` python
mini = 9999999   # initial value of the minimum number
maxi = -999999   # initial value of the maximum number

print('Enter some numbers in the range 1 ... 1000')

while True:                           # potential endless loop
	number = int(input('Number:'))    # user input of an int-value
	if number<0 or number>1000:       # number in valid range?
		break                         #   no: exit the loop
	if number < mini:                 # new minimum?
		mini = number                 #   yes: save the new minimum value
	elif number > maxi:               # new maximum?
		maxi = number                 #   yes: save the new maximum value

# show the result
print('The biggest number was:',maxi)
print('The smallest number was:',mini)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections, break a loop     | worked-out-example | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-elif-statement  
loop-2: while-loop including break-statement  
  
#### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) write comments to the code
4) verbal explaination of the code

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

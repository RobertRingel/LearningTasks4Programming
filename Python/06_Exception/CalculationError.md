Topic: exceptions

## Learning Task: Calculation Error

The given Python code is able to calculate the average grading result for a group of students.
Read the code and run the program in a way that it causes to crash when preforming the average calculation.  
Add the appropriate exception handling to prevent the program crash in this dedicated calculation situation. Finally run the program again to proof the functionality of your implementation.  
Note: In case of an effective exception handling the very last print command will be performed even in the error situation, because the exception was handled and the program did not crash.

``` python
sum_marks = 0
n = 0
avg = -1
while True:
	name = input('Name:')
	mark = int(input('Mark (1..5):'))
	if name=='' or mark<1 or mark>5:
		break
	sum_marks = sum_marks + mark
	n = n +1

# >>>> Protect these two lines by exception handling <<<<
avg = sum_marks / n
print('Avg. grading level:',avg)

print('end.')
```

---------------------------------------

### Solution

``` python
sum_marks = 0
n = 0
avg = -1
while True:
	name = input('Name:')
	mark = int(input('Mark (1..5):'))
	if name=='' or mark<1 or mark>5:
		break
	sum_marks = sum_marks + mark
	n = n +1

try:
	avg = sum_marks / n
	print('Avg. grading level:',avg)
except ZeroDivisionError:
	print('Error during calculation')

print('end.')
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| implement basic exception handling             | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, calculation, data type  
branch-2: if including different OR tests  
loop-2: while-break loop  
excp-1: try-except

#### Learning Activities

1) read the given Python code 
2) run the program in order to test it  
3) implement exception handling for ZeroDivisionError
4) test the exception handling

#### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 5.6, Seiten 167-177

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
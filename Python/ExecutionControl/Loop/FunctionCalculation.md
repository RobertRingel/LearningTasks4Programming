### Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
x = float(input('x-Start:'))
end = float(input('x-End:'))
step = float(input('step:'))

while x<end:
	y = x**2+2*x+3
	print('x:',x,'y:',y)
	x = x + step
```

---------------------------------------
---------------------------------------

##### Solution

*Purpose of the program:*  
The program is used to calculate and print a series of function values of a squared equation for an interval of x-values entered by the user.

*Programming task*  
Write a Python program to calculate and print values x and y of the equation y = x²+2x+3
The user shall enter the interval (x-start and x-end) and the step distance for the x-values.


##### Previous Knowledge

- print, input, variable
- while-loop 
  
##### Learning Activities

1) read, run and understand the Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code


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
[//]: # "Task type: reverse task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

### Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

Finally feel free to write more comments to the code.

``` python
import random as rd          # import random number generator
numbers = []

while len(numbers) < 6:
	i = rd.randint(1,49)     # generate a random number
	while i in numbers:
		i = rd.randint(1,49)
	numbers.append(i)

numbers.sort()
lottery = tuple(numbers)
print(lottery)
```

---------------------------------------
---------------------------------------

##### Solution

*Purpose of the program:*  
The program is used to generate random numbers for the lottery game '1 out of 49'.

*Programming task*  
Write a Python program to generate random numbers for the lottery game '1 out of 49'. The generated numbers shall be 
sorted and stored in a data structure that prevents the numbers from any change. Finally the numbers shall be printed.

##### Previous Knowledge

- basics about list and tuple data structure
- nested loops
  
##### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

##### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 116-132

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Tuple data structures 

*Learning objective:*  
- conversion of a list to a tuple


[//]: # "learning objective: 1-tuple"
[//]: # "previous knowledge: 3-loop 1-list"

*Complexity:*  1-low 

*Task type:*  reverse task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0

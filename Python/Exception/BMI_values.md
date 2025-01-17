### Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
weight = int(input('Your weight [kg]:'))
height = float(input('Your height [m]:'))

if weight < 15 or weight > 150 or height < 1.0 or height > 2.0:
	raise ValueError('Input for weight or height is invalid to calculate the BMI')

bmi = weight/height**2
print('Your bmi:',bmi)
```

---------------------------------------
---------------------------------------

##### Solution

*Purpose of the program:*  
The program is used to calculate the body-mass-index - it will raise an exception in case of invalid user input.

*Programming task*  
Write a Python program to calculate and print the body-mass-index (weight/height**2) according to the user input of weight \[kg\] and height \[m\].
The programm shall raise an exception in case of invalid input data for weight or height.

##### Previous Knowledge

- basics of input-processing-output
- basic data types
- basic branches
  
##### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

##### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 5.6, Seiten 167-177

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Exceptions 

*Learning objective:*  
- understand basic exception handling

[//]: # "learning objective: 2-exception"
[//]: # "previous knowledge: 2-ipo 1-branch"

*Complexity:*  1-low 

*Task type:*  reverse task

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 01/2025            
License: CC BY-SA 4.0

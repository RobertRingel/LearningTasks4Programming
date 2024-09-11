### Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
print('Q1: Do you see any value in learning programming?')
q1 = int(input('1-not at all  2-at little  3-some  4-really benefitial  :'))

print('Q2: How much effort do you spend for learning programming?')
q2 = int(input('1-almost none  2-at little  3-some  4-significant       :'))

print('Q3: Have you had already some success in learning programming?')
q3 = int(input('1-no  2-at little  3-some  4-I make good progress       :'))

score = q1 + q2 + q3
if score > 9:
	disposition = 'really good'
elif score > 6:
	disposition = 'fair'
elif score > 3:
	disposition = 'basic'
elif score == 3:
	disposition = 'not helpful'
else:
	disposition = ''

if disposition != '':
	print('Your disposition in learning programming is:',disposition)
```

---------------------------------------
---------------------------------------

##### Solution

*Purpose of the program:*  
The program is used to evaluate the students disposition towards learning programming.

*Programming task*  
Write a Python program to evaluate the students disposition towards learning programming.  
The user has to answer the following three questions on a scale of 1,2,3,4 points. 

Q1: Do you see any value in learning programming?  
Q2: How much effort do you spend for learning programming?  
Q3: Have you had already some success in learning programming?  

The total disposition score is the sum of points for each question. The programm will print a final verbal statement related to the total score.


##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input  
- if-elif-else-statements 


##### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code


###### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 

----
[//]: # "Learning objective: Test and branch using if-else including conjunction"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: reverse task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

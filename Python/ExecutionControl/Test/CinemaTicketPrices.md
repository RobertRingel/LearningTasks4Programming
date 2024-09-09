### Learning Task: Cinema Ticket Price Calculation

Write a Python program to calculate Ticket Prices for Cinemas.  
There are tickets for kids, seniors and standard tickets. Make a definition of the individual ticket prices for these classes. Buying more than 4 kids tickets triggers a discount of 50% for all the kids tickets. Bying more than 5 standard tickets enables a 30% discount for all standard tickets.

Implement this selling and calculation approach.  
Compare your final code with the code of another student.

``` python
# Cinema ticket price calculator

... the students code to be written here
```

---------------------------------------
---------------------------------------

##### Solution

``` python
# Cinema ticket price calculator

KIDS_PRICE = 5.0
SEN_PRICE = 6.5
STD_PRICE = 9.0

kids = int(input('Number of kids tickets:'))
sen = int(input('Number of senior tickets:'))
std = int(input('Number of standard tickets:'))

valid = True
if kids<0 or sen<0 or std<0:
	valid = False

kids_rate = 1.0
std_rate = 1.0
if valid:
	if kids>4:
		kids_rate = 0.5
	if std>5:
		std_rate = 0.3
	price = kids*KIDS_PRICE*kids_rate + sen*SEN_PRICE + std*STD_PRICE*std_rate
	print('Your total ticket pric is EUR:', price)
else:
	print('Invalid input data.')
```

##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input  
- if-else-statement including and or-conjunctions
  
##### Learning Activities

1) get an understanding of the problem
2) develop a solution strategy - identifiy code sections
3) implement the program
4) run and test the new program
5) compare the solution with an other student


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Test and branch using if-else including conjunction"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2+ - normal ... high"
[//]: # "Task type: conventional task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

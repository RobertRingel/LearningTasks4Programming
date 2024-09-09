### Learning Task: German traffic fees for alc and drugs

The following program informs about potential fees when driving under drugs and alcohol in Germany. The regulations are as follows:   

Young drivers in the age of 18 to 21 will get a fee of 250 EUR in case of driving under drugs or alcohol. In case a driver has a THC level greater than 3.5ng the fee will be 500 EUR. In case this THC level of greater than 3.5ng is combined with any level of alcohol, the fee will be 1000 EUR.  

Read the following code and test it.  
Write commentes into the code.  
Fill the appropriate fee values into the gaps. 


``` python
age = int(input('Your age [years]:'))
alc = float(input('Your alcohol level [promille]:'))
thc = float(input('Your canabis THC level [ng]:'))

a18 = age >= 18 and age < 21
a21 = age >= 21

a05 = alc > 0.5
thc35 = thc > 3.5

if a21 and a05:
	print('Do not drive!')
elif a21 and thc35 and acl>0.0:
	print('Do not drive - your Fee will be .... EUR') 
elif a21 and thc35:
	print('Do not drive - your Fee will be .... EUR')
elif a18 and (thc>0 or alc>0):
	print('Do not drive - your Fee will be .... EUR')
elif a18 and alc == 0.0 and thc == 0.0:
	print('Great guy!')
else:
	if age>=18:
		print('Drive savely - be careful!')
	else:
		print('Get driven!')
```

---------------------------------------
---------------------------------------

##### Solution

``` python
# input age, alcohol and drug level
age = int(input('Your age [years]:'))
alc = float(input('Your alcohol level [promille]:'))
thc = float(input('Your canabis THC level [ng]:'))

# a18: true for a young driver 18 <= age < 21 years
a18 = age >= 18 and age < 21

#a21: true for an adult driver age >= 21
a21 = age >= 21

# a05: true for drunken driver
a05 = alc > 0.5

# thc35: true for driving under drugs
thc35 = thc > 3.5

if a21 and a05:                  # adult drunken person
	print('Do not drive!')
elif a21 and thc35 and acl>0.0:  # adult under drugs and alcohol
	print('Do not drive - your Fee will be 1000 EUR') 
elif a21 and thc35:              # adult under drugs
	print('Do not drive - your Fee will be 500 EUR')
elif a18 and thc>0:              # young driver und drugs
	print('Do not drive - your Fee will be 250 EUR')
elif a18 and alc == 0.0 and thc == 0.0:
	print('Great guy!')          # clean young driver
else:                            # none of the above
	if age>=18:
		print('Drive savely - be careful!')
	else:
		print('Get driven!')     # ... kids should not drive
```

##### Previous Knowledge

- print, input, variable
- if-elif-else-statement
- boolean expressions and boolean variables
  
##### Learning Activities

1) read and run the Python code
2) understand the purpose of the boolean variables
3) document the undetsanding of the code by written code comments
4) document the undetsanding of the code by correct fee values in the print statements

###### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 

----
[//]: # "Learning objective: Boolean variables and branches using if-elif"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: Worked-out-example"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

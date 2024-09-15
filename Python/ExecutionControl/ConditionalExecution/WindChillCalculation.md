### Learning Task: Wind-Chill-Factor

The following program calculates the Wind-Chill-Factor.  
The implemented equation is valid for a temperature range of -50 ... 50 °Fahrenheit and winds between 5 and 60 miles/h.  

Add some lines of code, to make sure the calculation will only be performed in case of valid input data. Otherwise an error message should be shown.

``` python
# wind chill calculation 
# for temperature in degree Fahrenheits and wind speed in miles per hour

# calculation constants
OFFSET = 35.74
F1 = 0.6215
F2 = -35.75
F3 = 0.4275
EXP = 0.16

temp = float(input('Air temperature [°F]:'))
wind = float(input('Wind speed [mi/h]:'))
wc = OFFSET + F1*temp + F2*wind**EXP + F3*temp*wind**EXP
print('Wind chill [°F]:', wc)
```

---------------------------------------
---------------------------------------

##### Solution

``` python
# wind chill calculation 
# for temperature in degree Fahrenheits and wind speed in miles per hour

# calculation constants
OFFSET = 35.74
F1 = 0.6215
F2 = -35.75
F3 = 0.4275
EXP = 0.16

temp = float(input('Air temperature [°F]:'))
wind = float(input('Wind speed [mi/h]:'))

if temp>=-50 and temp <=50 and wind>=5 and wind<=60:
	wc = OFFSET + F1*temp + F2*wind**EXP + F3*temp*wind**EXP
	print('Wind chill [°F]:', wc)
else:
	print('Invalid input value.')
```

##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input  
- if-else-statement including and conjunctions
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) add an variable values check using an if-else-statement
4) run and test the new program


###### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 41-48

----
[//]: # "Learning objective: Test and branch using if-else including conjunction"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: completion task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

### Learning Task: Wind-Chill-Factor

The following program calculates the Wind-Chill-Factor for the metric unit system.  
Read the code and run the code.  

Implement a similar program to be used in U.S. based on temperature input in degree Fahrenheit and windspeed in miles/hr. Test the new program!  

The related equation is defined as:  
$wc = 35.74+0.6215\cdot T-35.75\cdot v^{0.16}+0.4275\cdot v^{016}$

A temperature of 22° Fahrenheit and a wind speed of 10 mi/hr should give a wind chill of 11 °Fahrenheit.

``` python
# wind chill calculation 
# for temperature in degree celsius and wind speed in kilometers per hour

# calculation constants
OFFSET = 13.12
F1 = 0.6215
F2 = -11.37
F3 = 0.3965
EXP = 0.16

temp_c = float(input('Air temperature [°C]:'))
wind_kmh = float(input('Wind speed [km/h]:'))

wc = OFFSET + F1*temp + F2*wind**EXP + F3*temp*wind**EXP

print('Wind chill [°C]:', wc)
```

---------------------------------------
---------------------------------------

##### Solution

The program calculates the wind chill for a given temperature in degree Fahrenheit and a wind speed given in miles per hour.

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

##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input 
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) write a new Python program using adapted constants and input and output texts because of other variable units
4) run and test the new program


###### Supporting information

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel X, Seiten 

----
[//]: # "Learning objective: Understanding of variables, calculation and result printing"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: imitation task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

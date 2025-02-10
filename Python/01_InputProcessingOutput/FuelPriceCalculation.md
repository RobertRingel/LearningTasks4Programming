Topic: variables, calculations, printing  

## Learning Task: Fuel Price Calculation

The following program calculates the fuel price for a car trip of a certain distance.  

Read the code and run the program.

Change the code in a way, to allow the user to enter distance, fuel consumption and price instead of the initial variable settings.


``` python
dist = 35         # distance [km]
fuel_cons = 4.3   # fuel consumption [l/100km]
price = 1.56      # fuel price [EUR]

fuel_cost = 0.01*dist * fuel_cons * price

print('The fuel cost for this trip is:', fuel_cost)
```

---------------------------------------

### Solution

``` python
dist = int(input('driven distance [km]:'))
fuel_cons = float(input('avg. fuel consumption [l/100km]:'))
price = float(input('fuel price [EUR/l]:'))

fuel_cost = 0.01*dist * fuel_cons * price

print('The fuel cost for this trip is:', fuel_cost)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding input and numeric type conversion | completion task | 1 - low  |

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: type conversion for numeric input  
  
#### Learning Activities

1) read and run the Python code
2) obtain an understanding of the code
3) extent the code by input-statements and the propper type-conversion
4) delete the lines with the initial variable settings
5) run and test the extended program

#### Supporting information

[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32

[www.python-kurs.eu: Variablen](https://www.python-kurs.eu/python3_variablen.php)  

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  
Kapitel 2, Seiten 23-27

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

### Learning Task: Fuel Price Calculation

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
---------------------------------------

##### Solution

``` python
dist = int(input('driven distance [km]:'))
fuel_cons = float(input('avg. fuel consumption [l/100km]:'))
price = float(input('fuel price [EUR/l]:'))

fuel_cost = 0.01*dist * fuel_cons * price

print('The fuel cost for this trip is:', fuel_cost)
```

##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input 
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) extent the code by input-statements and the propper type-conversion
4) delete the lines with the initial variable settings
5) run and test the extended program


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Understanding of input and numeric type conversion"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: complition task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

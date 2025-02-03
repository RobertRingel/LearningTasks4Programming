Topic: variables, calculations, printing

## Learning Task: Distance between GPS co-ordniates

Implement a program to calculate the distance between two GPS points! It is assumed that the points distance is relatively close (some kilometers) and that they are in the same earth quadrant.

Note: Entering the coordinate data shall be done using the input-function. The calculation is based on the theorem of Pythagoras. There is no square-root-function available. Use the related power-function instead.

The following web page explains the concept in the section "Einfachste Entfernungsberechnung": https://www.kompf.de/gps/distcalc.html

Demonstrate your program to an other student and explain it!

---------------------------------------

### Solution

``` python
# This is a simple python demo to calculate the GPS distance 

print("*** Distance between two GPS coordinates ***")

lon1 = float(input("Point 1 - Longitude: "))
lat1 = float(input("Point 1 - Latitude : "))

lon2 = float(input("Point 2 - Longitude: "))
lat2 = float(input("Point 2 - Latitude:  "))

dx = 71.5 * (lon1 - lon2)
dy = 111.3 * (lat1 - lat2)
distance = (dx * dx + dy * dy) ** 0.5

print("Distance [km]: ",distance)
```

*Initial help:*  
![initial help](GPSDistCaluculation_H1.png)

*More help:*  
![more help](GPSDistCaluculation_H2.png)

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| problem solving using basic calculation        | conventional task | 1 - low      |  

#### Previous Knowledge

vcp-1: variables, calculations  
vcp-2: data types, type casting functions  
 
#### Learning Activities

1) read the task and discuss the problem 
2) note the equation of the theorem of Pythagoras
3) adopt the theorem of Pythagoras to the earth grid of your region
4) write appropriate Python code
5) test the Python program using known co-ordinates and distances
6) speek about your code with another student - add comments to the code

#### Supporting information
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_data_types.htm)  
[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:
Kapitel 2, Seiten 23-27 und Kapitel 3, Seiten 37-39

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
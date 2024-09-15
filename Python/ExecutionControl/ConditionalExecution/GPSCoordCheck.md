### Learning Task: Checking GPS co-ordinates

The following Python program calculates the distance between two GPS co-ordinates in Germany. 
The result is valid only for Germany and for relatively short distances.

Add Python commands to check, that the entered co-ordinates are likely located in Germany. And add a check that gives a warning message in case the distance is too far.

Germany is located inside:  
5.8 < longitude < 15  
47 < latitude < 54.9  

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

---------------------------------------
---------------------------------------

##### Solution

``` python
# This is a simple python demo to calculate the GPS distance 

MIN_LON = 5.8
MAX_LON = 15
MIN_LAT = 47
MAX_LAT = 54.9

print('*** Distance between two GPS coordinates in Germany ***')

lon1 = float(input('Point 1 - Longitude: '))
lat1 = float(input('Point 1 - Latitude : '))

lon2 = float(input('Point 2 - Longitude: '))
lat2 = float(input('Point 2 - Latitude:  '))

check_lon = lon1>=MIN_LON and lon1<=MAX_LON and lon2>=MIN_LON and lon2<=MAX_LON
check_lat = lat1>=MIN_LAT and lat1<=MAX_LAT and lat2>=MIN_LAT and lat2<=MAX_LAT

if check_lon and check_lat:
	dx = 71.5 * (lon1 - lon2)
	dy = 111.3 * (lat1 - lat2)
	distance = (dx * dx + dy * dy) ** 0.5

	print('Distance [km]: ',distance)
	if distance > 200:
		print('This distance is an estimation - real this distance will be longer.')
else:
	print('The co-ordinates are outside of Germany. Calculation not possible.')
```

##### Previous Knowledge

- print, input, calculations, boolean variables
- if-else-statement
  
##### Learning Activities

1) read and run the Python code
2) develop a strategy to implement the tests (boolean variables, location of the test commands)
3) implement the boolean variables and tests
4) run and test the final program


###### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 41-48 

----
[//]: # "Learning objective: Test and branch using if-else, use of boolean variables"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: completion task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
License: CC BY-SA 4.0

### Learning Task: Calculating GPS distance

The following function can be used to calculate the approximate distance for near-by GPS-points in Germany.
Read the code and its documentation.  

Implement three different calls for this function (straight-foreward, other values for the default arguments, make use of named arguments).

``` python
def calc_GPS_distance(lat1, lon1, lat2, lon2, lat_width=111.3, lon_width=71.5):
	"""
	Calculates the distance between two GPS co-ordinate points.
	The function uses a simple theorem of Pythagoras approach. 

	Args:
		lat1 (float): latitude of point 1
		lon1 (float): longitude of point 1
		lat2 (float): latitude of point 2
		lon2 (float): longitude of point 2
		lat_width(float) : width for 1 degree latitude [km]
		lon_width(float) : width for 1 degree longitude [km]

	Returns:
		float: the distance between the given GPS points [km]
	"""
	dx = lon_width * (lon1 - lon2)
	dy = lat_width * (lat1 - lat2)
	distance = (dx * dx + dy * dy) ** 0.5	
	return distance 

```

---------------------------------------
---------------------------------------

##### Solution

``` python
def calc_GPS_distance(lat1, lon1, lat2, lon2, lat_width=111.3, lon_width=71.5):
	"""
	Calculates the distance between two GPS co-ordinate points.
	The function uses a simple theorem of Pythagoras approach. 

	Args:
		lat1 (float): latitude of point 1
		lon1 (float): longitude of point 1
		lat2 (float): latitude of point 2
		lon2 (float): longitude of point 2
		lat_width(float) : width for 1 degree latitude [km]
		lon_width(float) : width for 1 degree longitude [km]

	Returns:
		float: the distance between the given GPS points [km]
	"""
	dx = lon_width * (lon1 - lon2)
	dy = lat_width * (lat1 - lat2)
	distance = (dx * dx + dy * dy) ** 0.5	
	return distance 


d = calc_GPS_distance(51.2, 14.3, 51.2, 14.4)
print(d)

d = calc_GPS_distance(51.2, 14.3, 51.2, 14.4, 121.5, 76.9)
print(d)

d = calc_GPS_distance(lat2=51.2, lon2=14.3, lat1=51.2, lon1=14.4)
print(d)
```

##### Previous Knowledge

- basics of input-processing-output
- basics of functions
  
##### Learning Activities

1) read the given Python code 
2) implement different approaches for function calls
3) test the program

##### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Functions 

*Learning objective:*  
- understand different ways of function calls

[//]: # "learning objective: 2-function"
[//]: # "previous knowledge: 1-ipo 1-function"

*Complexity:*  1-low 

*Task type:*  completion task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

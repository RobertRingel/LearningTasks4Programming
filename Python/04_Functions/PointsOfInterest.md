Topic: functions

## Learning Task: Points of interest

Write a Python program that uses a dictionary to store various points
of interest including location name and GPS co-ordinates. The user selects 
two of these points and the program calculates the distance and the bearing 
between them.

The Python code below shows the calculation approach - the distance calculation 
is an approximation for nearby points in Germany.  
Background information: https://www.kompf.de/gps/distcalc.html  

Use functions for the implementation of this task and do not forget to write a
function documentation based on Google docstyle.

``` python
# --- approximate GPS distance ---
AVG_LON = 71.5
AVG_LAT = 111.3
dx = AVG_LON * (lon1 - lon2)
dy = AVG_LAT * (lat1 - lat2)
distance = (dx * dx + dy * dy) ** 0.5

# --- bearing between 2 GPS points ---
dLon = (long2 - long1)
x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) \
    - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) \
    * math.cos(math.radians(dLon))
brng = numpy.arctan2(x,y)
brng = numpy.degrees(brng)
```

---------------------------------------

### Solution

``` python
import numpy
import math

gps_points = {'Opera' : (51.054, 13.735), 'Airport' : (51.128, 13.766), 
			  'Central Station' : (51.040, 13.731), 'Blue Wonder':(51.053, 13.809)}

def calculate_bearing(lat1, long1, lat2, long2):
    """
    Calculates the bearing between the two given GPS points.
    Args:
        lat1 (float): latitude of point 1
        lon1 (float): longitude of point 1
        lat2 (float): latitude of point 2
        lon2 (float): longitude of point 2

    Returns:
        float: the bearing between the given GPS points [°]
    """	
    dLon = (long2 - long1)
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(dLon))
    brng = numpy.arctan2(x,y)
    brng = numpy.degrees(brng)
    return brng

def calculate_distance(lat1, lon1, lat2, lon2, lat_width=111.3, lon_width=71.5):
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

def print_locations(points):
    """
    Prints a sorted list of GPS location names.

    Args:
        points (dictionary) : GPS locations as dictionary of name : (lat,lon)
    """
    names = sorted(points.keys())
    for name in names:
        print(name)


while True:
    print_locations(gps_points)
    loc1 = input('Start location: ')
    loc2 = input('Destination location: ')

    if loc1 in gps_points.keys() and loc2 in gps_points.keys():
        lat1, lon1 = gps_points.get(loc1)
        lat2, lon2 = gps_points.get(loc2)
        dist = calculate_distance(lat1, lon1, lat2, lon2)
        bear = calculate_bearing(lat1, lon1, lat2, lon2)
        print('Distance [km]:',dist)
        print('Bearing  [°] :' ,bear)
    elif loc1 == '' or loc2 == '':
        break
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| use functions in problem solving               | conventional task | 4 - complex     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, calculations  
branch-2: if-elif  
loop-1: while-break loop  
tuple-1: tuple definition  
dict-1, dict-3: define dictionary, dictionary stores tuple, access dictionary data, iterate dictionary  
func-1, func-2, func-3: using functions, using modules, default arguments  

#### Learning Activities

1) read the task and discuss the problem 
2) develop an idea to solve the task
3) write appropriate Python code
4) write in-line function documentation
5) test the Python program using known co-ordinates and distances

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
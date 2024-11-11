### Learning Task: GPS bearing

The following program calculates the bearing from one GPS point to the other GPS point.
The mathematical calculation is implemented with help of several mathematical functions provided by two Python modules.

Run the programm, read the code and identify the mathematical functions and the related modules.
Explain how these functions are used and what is required to use them in the code.

``` python
import numpy
import math

def get_bearing(lat1, long1, lat2, long2):
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
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) \
        - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) \
        * math.cos(math.radians(dLon))
    brng = numpy.arctan2(x,y)
    brng = numpy.degrees(brng)
    return brng

# --- main part ---
bear = get_bearing(51.2, 14.0, 51.1, 14.1)
print(bear,'°')
```

---------------------------------------
---------------------------------------

##### Solution

1) To use a function from a module it is required to import the module (import numpy and import math).
2) An imported function is used by the name of the module, followed by the function name and its arguments (e.g. numpy.arctan2(x,y) )

##### Previous Knowledge

- basics of functions
  
##### Learning Activities

1) run and read the given Python program
2) identify the module import
3) identify the use of module functions
4) explain the usage of the imported functions in the code

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
- understand the use of module functions

[//]: # "learning objective: 3-function"
[//]: # "previous knowledge: 1-function"

*Complexity:*  1-low 

*Task type:*  worked-out-example

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

Topic: exceptions

## Learning Task: Distance between GPS co-ordniates

Given is the following Python program to calculate the distance between two nearby GPS-points in Germany.  
Background information: https://www.kompf.de/gps/distcalc.html


Improve this code in a way that it is unlinkely to crash caused by user input. Make sure the the entered GPS-points are not too far from each other, because the calculation approach is only valid for points close to each other.  
Demonstrate your program to an other student and explain it!

``` python
print("*** Distance between two GPS coordinates ***")

def get_coordinates():
    lon1 = float(input("Point 1 - Longitude: "))
    lat1 = float(input("Point 1 - Latitude : "))

    lon2 = float(input("Point 2 - Longitude: "))
    lat2 = float(input("Point 2 - Latitude:  "))

    return lat1, lon1, lat2, lon2


LON_WIDTH = 71.5     # average [km] width of 1° longitude in Germany
LAT_WIDTH = 111.3    # average [km] width of 1° latitude in Germany

lat1, lon1, lat2, lon2 = get_coordinates()
dx = LON_WIDTH * (lon1 - lon2)
dy = LAT_WIDTH * (lat1 - lat2)
distance = (dx * dx + dy * dy) ** 0.5

print("Distance [km]: ",distance)
```

---------------------------------------

##### Solution

``` python
def get_coordinates():
    try:                     # protect risky type conversion to float                         
        lon1 = float(input("Point 1 - Longitude: "))
        lat1 = float(input("Point 1 - Latitude : "))

        lon2 = float(input("Point 2 - Longitude: "))
        lat2 = float(input("Point 2 - Latitude:  "))
    except:                  # catch type conversion errors
        raise RuntimeError('Entered data is not numeric!')   # raise an exception

    # raise an exception in case the co-ordinates are not close to each other
    if abs(lon1-lon2) > 2.0 or abs(lat1-lat2) > 2.0:
        raise RuntimeError('Distance between GPS-points is too large to use this calculation approach')

    return lat1, lon1, lat2, lon2


print("*** Distance between two GPS coordinates ***")

LON_WIDTH = 71.5     # average [km] width of 1° longitude in Germany
LAT_WIDTH = 111.3    # average [km] width of 1° latitude in Germany

try:                                            # protect risky user input
    lat1, lon1, lat2, lon2 = get_coordinates()
except Exception as err:                        # catch error and print message
    print('There is an error:')
    print(err)
else:
    dx = LON_WIDTH * (lon1 - lon2)
    dy = LAT_WIDTH * (lat1 - lat2)
    distance = (dx * dx + dy * dy) ** 0.5
    print("Distance [km]: ",distance)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| implement exception handling                   | completion task | 3 - high       |  

##### Previous Knowledge

vcp-1, vcp-2: print, input, variable, calculations  
branch-1: basic if  
fun-1, func-3: basic function usage, multiple result values  
excp-1, excp-2: try-except, raise various exceptions
  
##### Learning Activities

1) read the given Python code 
2) identify potential risks and error situations in the code
3) improve the code by adding exception handling statements
4) test the Python program 
5) speek about your code with another student - add comments to the code

##### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 5.6, Seiten 167-177

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

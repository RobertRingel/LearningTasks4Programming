Topic: functions

## Learning Task: GPS distance

The following Python program can be used to calculate the approximate distance for near-by GPS-points in Germany.
Read the code, run the code and understand it.  
Then change the function in a way, that it will make use of default parameters to replace the global constants LAT_WIDTH and LON_WIDTH.
Finally test your implementation.

``` python
LAT_WIDTH = 111.3   # avg. width of 1° latitude in Germany
LON_WIDTH = 71.5    # avg. width of 1° longitude in Germany

def calc_GPS_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two GPS co-ordinate points.
    The function uses a simple theorem of Pythagoras approach. 

    Args:
        lat1 (float): latitude of point 1
        lon1 (float): longitude of point 1
        lat2 (float): latitude of point 2
        lon2 (float): longitude of point 2

    Returns:
        float: the distance between the given GPS points [km]
    """
    dx = LON_WIDTH * (lon1 - lon2)
    dy = LAT_WIDTH * (lat1 - lat2)
    distance = (dx * dx + dy * dy) ** 0.5	
    return distance 

d = calc_GPS_distance(51.2, 14.3, 51.2, 14.4)
print(d)
```

---------------------------------------

### Solution

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
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understand function default arguments          | completion task | 1 - low        | 

#### Previous Knowledge

vcp-1: print, variable  
func-1, func-2: basic function call and implementation, default arguments
  
#### Learning Activities

1) run and read the given Python code 
2) change the function implementation to use default parameters
3) test the program
4) update the function documentation regarding the default parameters

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

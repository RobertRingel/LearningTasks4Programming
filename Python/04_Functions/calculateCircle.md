Topic: functions

## Learning Task: Calculate circle

Implement the function 'calculate_circle' according to the given function documentation in the code below.
Implement the related function call as well to test the function.  

Finally run the programm and explain it to another student.

``` python
def calculate_circle..... :
    """
    Calculates area and perimeter of a circle.

    Args:
        diameter (float): the diameter of the circle

    Returns:
        float : the area of the circle
        float : the perimeter of the circle
    """

    ... implement the function ...

# --- main code ---	


... call the function ...
... show results ...

```

---------------------------------------

### Solution

``` python
def calculate_circle(diameter):
    """
    Calculates area and perimeter of a circle.

    Args:
        diameter (float): the diameter of the circle

    Returns:
        float : the area of the circle
        float : the perimeter of the circle
    """
    area = diameter * diameter * 3.14/4.0
    perimeter = 3.14 * diameter
    return area, perimeter

# --- main code ---	

a, p = calculate_circle(10.0)
print('Area:', a)
print('Perimeter:', p)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| functions with multiple return values          | conventional task | 1 - low      |  

#### Previous Knowledge

vcp-1: print, variable  
func-1, func-2: basic function call and implementation, multiple return values

#### Learning Activities

1) read the given Python function documentation
2) implement the function as specified in the documentation
3) run the program in order to test it
4) explain the program to another student

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

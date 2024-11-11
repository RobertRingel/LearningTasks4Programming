### Learning Task: Module planimetry

The listed code below shows the implementation of the module planimetry.py and its usage in another Python program.  

Read the code and run it to develop an understanding. Then extend the code by two functions to calculate the area 
and the perimeter of a circle. Finally call these two circle functions from another program to test them.

``` python
# -----------------------------------------------------------
# module: planimetry.py
#         provides functions for basic geometric calculations
# -----------------------------------------------------------

def rect_triangle_area(a,b):
    """
    Calculates the area of a right-angled triangle.

    Args:
        a (int or float) : length of side a
        b (int or float) : length of side b

    Returns:
        int or float : the area of the triangle
    """
    area = a * b / 2.0
    return area

def rect_triangle_extent(a, b):
    """
    Calculates the extent of a right-angled triangle.

    Args:
        a (int or float) : length of side a
        b (int or float) : length of side b

    Returns:
        int or float : the extent of the triangle
    """
    c = ((a*a) + (b*b))**0.5
    ext = a + b + c
    return ext

def rectangle_area(a, b):
    """
    Calculates the area of a rectangle.

    Args:
        a (int or float) : length of side a
        b (int or float) : length of side b

    Returns:
        int or float : the area of the rectangle
    """
    area = a * b
    return area

def rectangle_extent(a, b):
    """
    Calculates the extent of a rectangle.

    Args:
        a (int or float) : length of side a
        b (int or float) : length of side b

    Returns:
        int or float : the extent of the rectangle
    """
    ext = 2*a + 2*b
    return ext

# --- end of module implementation ---

# --- Python program to perform geometric calculations ---
import planimetry as pl

a = 10
b = 5

area_triang = pl.rect_triangle_area(a,b)
area_rect = pl.rectangle_area(a, b)

print(area_triang)
print(area_rect)
```
---------------------------------------
---------------------------------------

##### Solution

``` python
# --- extension of the module planimetry.py

def circle_area(d):
    """
    Calculates the area of a circle.

    Args:
        d (int or float) : diameter of the circle

    Returns:
        float : the area of the circle
    """
    area = 3.14 * d * d / 4.0
    return area

def circle_perimeter(d):
    """
    Calculates the perimeter of a circle.

    Args:
        d (int or float) : diameter of the circle

    Returns:
        float : the perimeter of the circle
    """
    perimeter = 3.14 * d
    return perimeter

# --- Python program to perform geometric calculations ---
import planimetry as pl

d = 10

area_circ = pl.circle_area(d)
perim_circ = pl.circle_perimeter(d)

print(area_circ)
print(perim_circ)
```

##### Previous Knowledge

- basics of input-processing-output
- basic data types
  
##### Learning Activities

1) read the given Python code and the function documentation
2) extend the function implementation of the module
3) extend the main code to test the new function implementations
4) run the program in order to test it

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
- write functions in a module

[//]: # "learning objective: 3-function"
[//]: # "previous knowledge: 2-ipo"

*Complexity:*  2-normal 

*Task type:*  imitation task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

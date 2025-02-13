Topic: functions

## Learning Task: Basic Chart Plot

The code below provides the import of the matplotlib.pyplot module that provides many functions for chart plotting.
Besides this the code has two data series to be plotted.
Complete the code to plot a basic line chart and make use of the following functions:  
plot, xlabel, ylabel, title and show.  

You should read the following pyplot function documentation pages:  
https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html  
https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

Implement the chart plotting functionality, test the program and compare your solution with another student.

``` python
import matplotlib.pyplot as plt

# data series 1
xpoints1 = [1, 8, 12, 17]
ypoints1 = [3, 10, 11, 19]

# data series 2
xpoints2 = [2, 9, 13, 18]
ypoints2 = [3, 10, 11, 19]

# plot the line chart 


```

---------------------------------------

### Solution

``` python
import matplotlib.pyplot as plt

# data series 1
xpoints1 = [1, 8, 12, 17]
ypoints1 = [3, 10, 11, 19]

# data series 2
xpoints2 = [2, 9, 13, 18]
ypoints2 = [3, 10, 11, 19]

# plot the line chart 
plt.plot(xpoints1, ypoints1, xpoints2, ypoints2)
plt.xlabel('x-Values')
plt.ylabel('y-Values')
plt.title('My first chart')
plt.show()
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| use functions of an unknown Python module      | completion task | 2 - normal     |  

#### Previous Knowledge

list-1: define lists  
func-1, func-3: basic function call, using modules

#### Learning Activities

1) read the given Python code 
2) read the pyplot function documentation web pages
3) implement the chart plotting Python code
4) run and test the implementation
5) compare the solution with another student

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  License: CC BY-SA 4.0
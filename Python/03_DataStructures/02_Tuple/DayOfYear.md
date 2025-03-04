Topic: data structures - tuple

## Learning Task: Day of year

The following program shall be used to calculate the number of the day in the year for a particular date entered by the user.

Read the given code and get an understandig.  
Then add the missing lines and test the program.

``` python
# --- calculate the day number of a particular day in the year ---

# a tuple to store all the leap years
leap_years = (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,	
			  1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,	
			  2020,2024,2028,2032,2036,2040,2044,2048)

# a tuple to store all the day counts for the different months
mon_days = ...

print('Enter the desired date!')
year = int(input('year:'))
mon = int(input('month:'))
day = int(input('day:'))

d = day
i = 0
while i<(mon-1):                        # sum up the days for the months
	...
	...

if (year in leap_years) and mon>2:      # is it a leap year?
	...                                 # yes: add 1 day

print('This date represents the day number',d,'in this year.')
```

---------------------------------------

### Solution

``` python
# --- calculate the day number of a particular day in the year ---

# a tuple to store all the leap years
leap_years = (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,	
			  1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,	
			  2020,2024,2028,2032,2036,2040,2044,2048)

# a tuple to store all the day counts for the different months
mon_days = (31,28,31,30,31,30,31,31,30,31,30,31)

print('Enter the desired date!')
year = int(input('year:'))
mon = int(input('month:'))
day = int(input('day:'))

d = day                                 # initialize day count variable
i = 0                                   # index to run over the months
while i<(mon-1):                        # sum up the days for the months
	d = d + mon_days[i]   
	i = i+1

if (year in leap_years) and mon>2:      # is it a leap year?
	d = d+1                             # yes: add 1 day

print('This date represents the day number',d,'in this year.')
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| access tuple elements with help of an index    | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data type  
branch-2: if using conjunction  
loop-1: basic while-loop  
tuple-1: define a tuple, access tuple by index

#### Learning Activities

1) read the code in order to get an understandig of it
2) define a tuple and access the items by use of an index
3) test the code by entering specific dates

#### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  Kapitel 4, Seiten 116-132

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

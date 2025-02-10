Topic: data structures - tuple

## Learning Task: Water level trend analysis

The following Python program can process a series of water level measured values in order to calculate a prediction for the next measured value.

Read and run the given Python code. Then write comments to the lines. Highlight the section of the code that is used to extract the data items out of a tuple.
Explain your code comments to another student.

``` python
# --- forecast river levels ---

measure = [('DD-City','2020-12-01 10:15',450),('DD-City','2020-12-01 11:15',455),
		   ('DD-City','2020-12-01 12:15',460),('DD-City','2020-12-01 13:15',470),
		   ('DD-City','2020-12-01 14:15',475),('DD-City','2020-12-01 15:15',485),
		   ('DD-City','2020-12-01 16:15',490),('DD-City','2020-12-01 17:15',500),
		   ('DD-City','2020-12-01 18:15',501),('DD-City','2020-12-01 19:15',503),
		   ('HH-City','2020-12-01 10:15',650),('HH-City','2020-12-01 11:15',651),
		   ('HH-City','2020-12-01 12:15',651),('HH-City','2020-12-01 13:15',653),
		   ('HH-City','2020-12-01 14:15',655),('HH-City','2020-12-01 15:15',657),
		   ('HH-City','2020-12-01 16:15',660),('HH-City','2020-12-01 17:15',663),
		   ('HH-City','2020-12-01 18:15',667),('HH-City','2020-12-01 19:15',670)]

selected_location = input('Select location (DD-City or HH-City):')

level = []

for rec in measure:
	loc, time, lev = rec
	if loc == selected_location:
		level.append(lev)

i = 2
Wi = 0.5
Wi1 = 0.3
Wi2 = 0.2
n = len(level)

while i < n:
	fc = Wi2*level[i-2] + Wi1*level[i-1] + Wi*level[i]
	if i+1 < n:
		print('forecast:',fc,' value:',level[i+1]) 	
	i=i+1
```

---------------------------------------

### Solution

``` python
# --- forecast river levels ---
# the data series of measured river level values
measure = [('DD-City','2020-12-01 10:15',450),('DD-City','2020-12-01 11:15',455),
		   ('DD-City','2020-12-01 12:15',460),('DD-City','2020-12-01 13:15',470),
		   ('DD-City','2020-12-01 14:15',475),('DD-City','2020-12-01 15:15',485),
		   ('DD-City','2020-12-01 16:15',490),('DD-City','2020-12-01 17:15',500),
		   ('DD-City','2020-12-01 18:15',501),('DD-City','2020-12-01 19:15',503),
		   ('HH-City','2020-12-01 10:15',650),('HH-City','2020-12-01 11:15',651),
		   ('HH-City','2020-12-01 12:15',651),('HH-City','2020-12-01 13:15',653),
		   ('HH-City','2020-12-01 14:15',655),('HH-City','2020-12-01 15:15',657),
		   ('HH-City','2020-12-01 16:15',660),('HH-City','2020-12-01 17:15',663),
		   ('HH-City','2020-12-01 18:15',667),('HH-City','2020-12-01 19:15',670)]

selected_location = input('Select location (DD-City or HH-City):')  # user selects one location

level = []                            # list of water levels for the selected location

for rec in measure:                   # iterate all measured data
	loc, time, lev = rec              # extract a tuple of measured data <<<<<<<
	if loc == selected_location:      # loc is selected location?
		level.append(lev)             # yes: store the level value

# calculate the forecasts
i = 2                                 # starting index to access level values
Wi = 0.5                              # weight of last value
Wi1 = 0.3                             # weight of value before last value
Wi2 = 0.2                             # weight for value two values before the last one
n = len(level)                        # number of measured values

while i < n:                                              # loop over all level data     
	fc = Wi2*level[i-2] + Wi1*level[i-1] + Wi*level[i]    # calculate the next forecast value
	if i+1 < n:
		print('forecast:',fc,' value:',level[i+1]) 	      # print forecast and related real value
	i=i+1                                                 # increment index
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| data extraction from tuples, using list of tuples | worked-out example | 3 - high       |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-1: simple if  
loop-1: basic while-loop  
list-1: list append, list index, for-iteration  
tuple-2: list of tuples, data extraction from tuple  

#### Learning Activities

1) read and run the code in order to get an understandig of it
2) write comments to explain the code
3) highlight the tuple extraction
4) explain the code to another student to validate the understanding

#### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 116-132

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

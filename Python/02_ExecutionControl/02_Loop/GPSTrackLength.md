Topic: controlling program execution - loop

## Learning Task: Length of a GPS track

Design and implement a Python program that can be used to calculate the length of a GPS track.  
The user will enter a sequence of GPS co-ordinates and the program will calculate the distance between the individual track points and cumulate them to the length of the track.  
Demonstrate your program to an other student and explain it!

Help: The following lines of code demonstrates the GPS distance calculation for two track points in Germany (AVG_LAT, AVG_LON).

``` python
AVG_LON = 71.5
AVG_LAT = 111.3
dx = AVG_LON * (lon1 - lon2)
dy = AVG_LAT * (lat1 - lat2)
distance = (dx * dx + dy * dy) ** 0.5
```

---------------------------------------

### Solution

``` python
# --- Length of a GPS-Track ---

AVG_LON = 71.5          # average distance [km] for 1 degree longitude
AVG_LAT = 111.3         # average distance [km] for 1 degree latitude

print('*** Length of a GPS-Track ***')

track = 0.0             # length of the track [km]
n = 0                   # number of a track point

print('Enter start point co-ordinates:')
lon1 = float(input('Point 1 - Longitude: '))
lat1 = float(input('Point 1 - Latitude : '))

while True:                                      # loop over series of track points
	n = n +1                                     # increment track point number
	print('Track point no.:',n)
	lon2 = float(input('Point 2 - Longitude: '))
	lat2 = float(input('Point 2 - Latitude : '))

	if lon2>1000 or lat2>1000:                   # terminate the input loop
		break

    # perform the calculation
	dx = AVG_LON * (lon1-lon2)
	dy = AVG_LAT * (lat1-lat2)
	distance = (dx*dx + dy*dy) **0.5
	track = track + distance

	print('Distance [km]:', distance)

    # save the current track point co-ordinates as the last ones!
	lon1 = lon2
	lat1 = lat2

print('Track length [km]:', track)
```

***Help for students to get an idea about to code structure***
``` python
# --- Length of a GPS-Track ---

AVG_LON = 71.5          # average distance [km] for 1 degree longitude
AVG_LAT = 111.3         # average distance [km] for 1 degree latitude

print('*** Length of a GPS-Track ***')

                        # length of the track [km]
                        # number of a track point

print('Enter start point co-ordinates:')
lon1 =  
lat1 =  

while                                            # loop over series of track points
	                                             # increment point number
	print('Track point no.:',n)
	lon2 = float(input('Point 2 - Longitude: '))
	lat2 = float(input('Point 2 - Latitude : '))

	if                                           # terminate the input loop
		break

    # perform the calculation


	distance = (dx*dx + dy*dy) **0.5
	track = 

	print('Distance [km]:', distance)  

    # save the current track point co-ordinates as the last ones!

	lat1 = lat2

print('Track length [km]:', track)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections, break a loop     | conventional task | 3 - high     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data types, calculations  
branch-1: if-statement  
loop-2: while-loop including break-statement  

#### Learning Activities

1) read the task and discuss the problem 
2) develop an idea to solve the task
3) write appropriate Python code
4) test the Python program using known co-ordinates and distances
5) speek about your code with another student - add comments to the code

#### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
[tutorialspoint.com: break-Statement](https://www.tutorialspoint.com/python/python_break_statement.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 7, pages 118-121

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 60-62

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
Lizenz: CC BY-SA 4.0

Topic: data structures - tuple

## Learning Task: GPS track processing

Write a Python program that is able to process the data of a series of GPS track points in order to calculate the total track length and to show the entire track data.  
The user will enter the name of a track point, a timestamp as well as its latitude and longitude for the series of all the passed track points. The programm shall store this data and it shall calculate the total path length.
At the end the entiere track shall be printed.

The data structure for this program shall be a list of tuples, where the tuple shall store the track point data.

Write the code, test the program and add comments to the code. Finally compare your solution with the one of another student.

Help: The following lines of code demonstrate the GPS distance calculation for two track points in Germany (AVG_LAT, AVG_LON).  
Background information: https://www.kompf.de/gps/distcalc.html

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
AVG_LON = 71.5                                     # avg. width of 1° longitude in Germany
AVG_LAT = 111.3                                    # avg. width of 1° latitude in Germany
length = 0.0                                       # length of the track
track = []                                         # list of track points
i = 1                                              # track index

while True:
	print('Track point:',i)                        # user will enter track point data
	name = input('Name of the location (end will stop the program):')
	if name == 'end':
		break
	time = input('Timestamp (hh:mm):')
	lat = float(input('Latitude :'))
	lon = float(input('Longitude:'))
	
	record = (name,time,lat,lon)                   # store track point data as tuple
	track.append(record)                           # append track point to the track list
	if i>1:
		dx = AVG_LON * (lon1 - lon)                # calculate distance between two track points
		dy = AVG_LAT * (lat1 - lat)
		dist = (dx*dx + dy*dy) **0.5        
		length = length + dist                     # cumulate the track length
		print(dist,'km')
	lon1 = lon                                     # save current point longitude
	lat1 = lat                                     # save current point latitude
	i = i +1                                       # increment track point counter
print('---------------------------------')
print('Length of the track',length,'km')           # print track length
print(track)                                       # print track list

```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| definition of tuple, use list to store tuples  | conventional task | 4 - complex    |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, calculation, data type  
branch-1: simple if  
loop-2: while-loop using break  
list-1: list append  
tuple-1, tuple-2: define a tuple, list of tuples  
  
#### Learning Activities

1) read the task and discuss the problem 
2) develop an idea to solve the task
3) write appropriate Python code
4) test the Python program using known co-ordinates and distances
5) speek about your code with another student - add comments to the code

#### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 116-132

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

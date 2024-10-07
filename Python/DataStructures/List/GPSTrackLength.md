### Learning Task: GPS-Track length

Write a Python program that has a list of GPS track points (name, longitude, latitude). The program shall process all the track points to calculate the distance from point to point. It shall print these distancces and finally the overall track length.

Write the code, test the program and add comments to the code. Finally compare your solution with the one of another student.


Help: The following lines of code demonstrate the GPS distance calculation for two track points in Germany (AVG_LAT, AVG_LON).

``` python
AVG_LON = 71.5
AVG_LAT = 111.3
dx = AVG_LON * (lon1 - lon2)
dy = AVG_LAT * (lat1 - lat2)
distance = (dx * dx + dy * dy) ** 0.5
``` 

---------------------------------------
---------------------------------------

##### Solution
``` python
# the GPS track data as a sequence of track points name,lon,lat,name,lon,lat,...
track = ['Airport', 13.7652, 51.1306, 'Main Station', 13.7303, 51.0408, 'University', 13.7351, 51.0372, 'Blue Wonder', 13.8095, 51.0533]

print('*** Length of a GPS track ***')

LON_KM = 71.5                   # avg. width of 1° longitude in Germany
LAT_KM = 111.3                  # avg. width of 1° latitude in Germany
length = 0                      # length of the track
pos=0                           # track index

loc1 = track[pos*3]             # name of track point 1
lon1 = track[pos*3+1]           # longitude of track point 1
lat1 = track[pos*3+2]           # latitude of track point 1
pos = pos+1

while pos*3 < len(track):                    # loop over all track points
	loc2 = track[pos*3]                      # name of next track point
	lon2 = track[pos*3+1]                    # longitude of next track point
	lat2 = track[pos*3+2]                    # latitude of next track point

	dx = LON_KM * (lon1 - lon2)
	dy = LAT_KM * (lat1 - lat2)
	distance = (dx*dx + dy*dy) **0.5         # distance between track point
	
	length = length + distance               # total length

	print(loc1,'>', loc2,':',distance,'km')  # print track point names and distance

	pos = pos+1                              # increment index
	loc1 = loc2                              # last location = current location
	lon1 = lon2                              # last longitude = current longitude
	lat1 = lat2                              # last latitude = current latitude

print('Total distance:',length,'km')         # finally: print total track length
```

***Help for students to get an idea about to code structure***
``` python
# the GPS track data as a sequence of track points name,lon,lat,name,lon,lat,...
track = ['Airport', 13.7652, 51.1306, 'Main Station', 13.7303, 51.0408, 'University', 13.7351, 51.0372, 'Blue Wonder', 13.8095, 51.0533]

print('*** Length of a GPS track ***')

# --- important initial variable settings ---
LON_KM = 71.5                   # avg. width of 1° longitude in Germany
LAT_KM = 111.3                  # avg. width of 1° latitude in Germany
length = 0                      # length of the track
pos=0                           # track index

# --- get all data for track point 1 ---
loc1 =                          # name of track point 1
lon1 =                          # longitude of track point 1
lat1 =                          # latitude of track point 1
pos = pos+1

# --- loop over all track points ---
while       :
	# --- get all data for the next track point  ---	
	loc2 = 
	lon2 = 
	lat2 = 

	# --- calculate distance between two track points



	
	                            # sum up total length

	                            # print track point names and distance

	                            # increment index
	# --- store last track point data
	loc1 = 
	lon1 = 
	lat1 = 

print('Total distance:',length,'km')         # finally: print total track length
```

##### Previous Knowledge

- basic list operations 
- loops and branches
- basics of GPS distance calculation (e.g. https://www.kompf.de/gps/distcalc.html)
  
##### Learning Activities

1) read the task and discuss the problem 
2) develop an idea to solve the task
3) write appropriate Python code
4) test the Python program using known co-ordinates and distances
5) speek about your code with another student - add comments to the code

###### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 109-116

----
[//]: # "Learning objective: problem solving"
[//]: # "Topic: List data structures"
[//]: # "Complexity: 3 - high"
[//]: # "Task type: conventional task / complex task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0

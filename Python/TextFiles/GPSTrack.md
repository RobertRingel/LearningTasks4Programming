### Learning Task: GPS track

The following Python program can be used to calculate the length of a GPS track.
In the given code the track data is stored in the list 'track'.  

You should implement a section of Python code to read the track data from the
text file 'GPSTrack.txt' into the list variable 'track'.

First open the text file to understand its content. Then implement the required
Python commands to read the data from the text file. Do not forget to write
comments to your code.  
Run the program to test it.  
Finally explain your implementation to another student.

``` python
# the GPS track data as a sequence of track points name,lon,lat,name,lon,lat,...
track = ['Airport', 13.7652, 51.1306, 'Main Station', 13.7303, 51.0408, 'University', 13.7351, 51.0372, 'Blue Wonder', 13.8095, 51.0533]

# ----- read track file -----
#  ... to be implemented ...


# ----- perform track length calculation -----
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

---------------------------------------
---------------------------------------

#### Solution

``` python
# the GPS track data as a sequence of track points name,lon,lat,name,lon,lat,...
track = []                           # initalize an empty track list

# ----- read track file -----

file_name = 'GPSTrack.txt'           # define the file name
track_file = open(file_name, 'r')    # open file for reading

while True:                          # loop to read the file line by line
    line = track_file.readline()     # read on line of data
    line = line.strip('\n')          # remove line break from line string
    if line == '':                   # empty line -> stop reading
        break
    data = line.split(';')           # split line items by ;
    location = data[0]               # get location
    lon = float(data[1])             # get longitude
    lat = float(data[2])             # get latitude
    
    # append track data
    track.append(location)           
    track.append(lon)
    track.append(lat)

track_file.close()                   # close file

# ----- perform track length calculation -----
print('*** Length of a GPS track ***')
...
...
```

##### Previous Knowledge

- basics of loops and branches
- basics of lists
  
##### Learning Activities

1) understand content of the text file
2) implement the required Python commands to read the data from the text file
3) run and test the implemented Python code
4) write comments to the written code
5) explain the code to another student

##### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  
Kapitel 8, Seiten 257-270

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Text files

*Learning objective:*  
- read text file into data structure

[//]: # "learning objective: 1-files"
[//]: # "previous knowledge: 2-ipo 1-list 1-branch 1-loop"

*Complexity:*  2-normal

*Task type:*  completion task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
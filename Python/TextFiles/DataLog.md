### Learning Task: Data log

The following Python program reads the data log file 'FreeFall.txt' of an
physic's experiment. The data that has been read will be plotted as a very
basic chart.

First open the log file to understand its content. Then read the code and run
it to obtain an understanding.  
You should write comments to the code to demonstrate your understanding.  
Finally compare your comments with another student.

``` python
import matplotlib.pyplot as plt   # import library for chart plotting

file_name = 'FreeFall.txt'
log_file = open(file_name, 'r')

data_log = []

while True:
    line = log_file.readline()
    line = line.strip('\n')
    if line == '':
        break
    data = line.split(';')
    for item in data:
        item = float(item)
        data_log.append(item)

log_file.close()

# --- plot chart ---
t = data_log[0::3]
s = data_log[2::3]

plt.plot(t, s)                   # plot the chart
plt.show()                       # display the plot
```

---------------------------------------
---------------------------------------

#### Solution

``` python
import matplotlib.pyplot as plt   # import library for chart plotting

file_name = 'FreeFall.txt'        # define the file name
log_file = open(file_name, 'r')   # open the log file for reading

data_log = []                     # list of data

while True:                       # loop to read file line by line
    line = log_file.readline()    # read one line from the file
    line = line.strip('\n')       # remove line break from the line
    if line == '':                # line is empty -> end reading loop
        break
    data = line.split(';')        # split line items using ;
    for item in data:             # iterate all line items
        item = float(item)        #    convert to float
        data_log.append(item)     #    append to list of data

log_file.close()                  # close the log file

# --- plot chart ---
t = data_log[0::3]                # get sub-list of time values
s = data_log[2::3]                # get sub-list of s-values (distance)

plt.plot(t, s)                    # plot the chart
plt.show()                        # display the plot
```

##### Previous Knowledge

- basics of loops and branches
- basics of lists
  
##### Learning Activities

1) understand content of the text file
2) read and run the given Python code
3) write comments to the code
4) explain the code to another student

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
- understand reading text files into data structure

[//]: # "learning objective: 2-files"
[//]: # "previous knowledge: 1-list 1-branch 1-loop"

*Complexity:*  2-normal

*Task type:*  worked-out example

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
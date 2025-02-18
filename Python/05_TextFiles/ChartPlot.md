Topic: text files

## Learning Task: Chart plot

The following Python program takes a text file to read all chart plotting 
data used to plot a basic line chart.

Open the text file 'ChartPlot.cfg' to get an understanding of the provided
data. Then read the given Python code and write comments to the commands
used to read the data from the file.  
What data structure is used to store the data that has been read from the file?  
What is the purpose of the 'prepare x-values' and 'prepare y-values' code 
sections?

``` python
import matplotlib.pyplot as plt

file_name = 'ChartPlot.cfg'
cfg_file = open(file_name, 'r')
cfg_data = {}

while True:
    line = cfg_file.readline()
    line = line.strip('\n')
    if line == '':
        break
    key, value = line.split(':')
    cfg_data[key] = value.strip()   

cfg_file.close()

# --- prepare x-values for chart plotting
val = cfg_data.get('x-data')
if val == None:
    print('Missing x-values')
else:
    num_values = []
    val = val.split(' ')
    for v in val:
        v = float(v)
        num_values.append(v)        
    cfg_data['x-data'] = num_values
    print('x-values:', num_values)

# --- prepare y-values for chart plotting
val = cfg_data.get('y-data')
if val == None:
    print('Missing y-values')
else:
    num_values = []
    val = val.split(' ')
    for v in val:
        v = float(v)
        num_values.append(v)        
    cfg_data['y-data'] = num_values
    print('y-values:', num_values)

# --- perform chart plotting
title = cfg_data.get('title')
xlabel = cfg_data.get('x-label')
ylabel = cfg_data.get('y-label')
x = cfg_data.get('x-data')
y = cfg_data.get('y-data')
plt.plot(x, y)                          # plot the chart
plt.xlabel(xlabel)                      # add X-axis label
plt.ylabel(ylabel)                      # add Y-axis label
plt.title(title)                        # add title
plt.show()                              # show the plot
```

---------------------------------------

### Solution

``` python
import matplotlib.pyplot as plt

file_name = 'ChartPlot.cfg'          # name of the text file
cfg_file = open(file_name, 'r')      # open text file for reading
cfg_data = {}                        # dictionary for data from text file

while True:                          # read file line by line
    line = cfg_file.readline()       # read one line
    line = line.strip('\n')          # remove line break from line
    if line == '':                   # empty line -> stop reading
        break
    key, value = line.split(':')     # split line at ':' into key and value 
    cfg_data[key] = value.strip()    # store line data in dictionary

cfg_file.close()                     # close text file

...
```

What data structure is used to store the data that has been read from the file?  
A dictionary is used to store the data from the file. Every text line will be stored
in the dictionary. The key is the information left of the colon character. The
value is all data right to it. The initial value after reading  is just a
string.  

What is the purpose of the 'prepare x-values' and 'prepare y-values' code 
sections?  
These parts of the code are used to transform the strings that store the x-values
and the y-values into lists. Every number will be transformed to an individual
list item of data type float. The result of the transformation is shown by a
print command.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| reading text files into a data structure       | worked-out example | 3 - high       |

#### Previous Knowledge

vcp-1, vcp-2: print, variable, data type conversion  
str-2: important string operations  
branch-1, branch-2: basic if-statement, if-else-statement  
loop-2: while-break loop  
func-1, func-3: import modules, call functions  
list-1: basic list operations incl. iteration  
dict-1: basic dictionary operations
file-1: basic file reading  

#### Learning Activities

1) read and understand the related text file
2) read the given Python code
3) test and run the program
4) write comments to the lines used to read data from file
5) answer the given questions

#### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 8, Seiten 257-270

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
Topic: text files

## Learning Task: Aphorism

The following Python program shall read quotes from a text file and it shall
print a randomly selected quote at the screen.

Read the code and obtain an understanding. After that, write the missing Python
file commands to read data from the text file. Finally run the program.

``` python
import random as rd                     # import random numbers library

file_name = 'Aphorism.txt'              # name of the text file
max_lines = 99                          # number of lines in the file
...                                     # open file for reading

line_no = rd.randint(1,max_lines)       # the line number to be shown

i=0                                     # line counter
while i<line_no:                        # read until desired line number
    i=i+1                               # increment line counter
    ...                                 # read line from file
    if line == '':                      # empty line -> stop reading
        break

print(line)                             # print line text

...                                     # close the file 
```

The quotes contained in the text file have been taken from this source:  
https://gist.github.com/robatron/a66acc0eed3835119817#file-quotes-txt

---------------------------------------

### Solution

``` python
import random as rd                     # import random numbers library

file_name = 'Aphorism.txt'              # name of the text file
max_lines = 99                          # number of lines in the file
quotes_file = open(file_name, 'r')      # open file for reading

line_no = rd.randint(1,max_lines)       # the line number to be shown

i=0                                     # line counter
while i<line_no:                        # read until desired line number
    i=i+1                               # increment line counter
    line = quotes_file.readline()       # read line from file
    if line == '':                      # empty line -> stop reading
        break

print(line)                             # print line text

quotes_file.close()                     # close the file
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| reading text files                             | completion task | 3 - high       |  

#### Previous Knowledge

vcp-1: print, variable  
branch-1: basic if  
loop-2: while-break loop  
func-1, func-3: import modules, call functions  
file-1: basic file reading  
  
#### Learning Activities

1) read the given Python code
2) write the missing Python commands to read data from file
3) test and run the program

#### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 8, Seiten 257-270

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
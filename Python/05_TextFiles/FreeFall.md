Topic: text files

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?
Write the text for a related programming task.

Finally feel free to write comments to the code.

``` python
# -----------------------------------------------------------------
# --- data log for free fall experiment in a 2m vacuum cylinder ---
# -----------------------------------------------------------------

g = 9.81
s = 0.0
t = 0.0
dT = 0.05

file_name = 'DataLog.txt'
log_file = open(file_name, 'w')

while s<2.0:
    v = g * t
    s = 0.5*g*t*t
    line = str(t)+';'+str(v)+';'+str(s)+'\n'
    log_file.write(line)
    t = t + dT

log_file.close()
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the data for a free fall experiment. The 
calculated data is written to a text file.

*Programming task*  
Write a Python program to calculate to data for a 2.00m free fall 
experiment. The calculated data shall be written to a text file named 
'DataLog.txt'. The calculation shall be performed in time steps of 0.05s. 
The text file shall contain one line per time step containing the time,
the speed and the distance of the fallen object.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| writing text files                             | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1: print, variables, calculations  
str-1: string concatenation  
loop-1: basic while loop  
file-1: basic file writing  

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 8, Seiten 257-270

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
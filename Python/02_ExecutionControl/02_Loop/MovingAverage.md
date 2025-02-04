Topic: controlling program execution - loop

## Learning Task: Moving average calculation

The following program takes a sequence of numbers as user input. Therefore it calculates the moving average over the last three numbers.

Read the program, run it and write comments to the significant lines in the code.  
Finally explain your understanding of the program to another student.

``` python
# Calculate the moving average
# ----------------------------

z3=0
z2=0
z1=0

while True:
    z = int(input("Number:"))    
    if z<0:                      
        break
   
    z3=z2
    z2=z1
    z1=z

    mavg = (z1+z2+z3)/3
    print(z3, z2, z1," mvg. avg.:", mavg)

print('Program finished.')
```

---------------------------------------

### Solution

``` python
# Calculate the moving average
# ----------------------------

# initialize variables to zero
z3=0
z2=0
z1=0

# loop to enter numbers and calculate moving average
while True:
    z = int(input("Number:"))    # get an integer value
    if z<0:                      # break the loop in case of negative value
        break
    # keep the last 3 values for calculation of the mvg. avg.    
    z3=z2
    z2=z1
    z1=z
    # calculate the moving avg.
    mavg = (z1+z2+z3)/3
    print(z3, z2, z1," mvg. avg.:", mavg)

print('Program finished.')
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections, break a loop     | worked-out-example | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-elif-statement  
loop-2: while-loop including break-statement  
  
#### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) write comments to the code
4) verbal explaination of the code

#### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
[tutorialspoint.com: break-Statement](https://www.tutorialspoint.com/python/python_break_statement.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 7, pages 118-121

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 60-62

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
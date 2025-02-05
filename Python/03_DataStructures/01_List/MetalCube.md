Topic: data structures - list

## Learning Task: Weight of metal cubes

The following Python program calculates the weight of different metal cubes.

Read the code, run the program, understand it and write comments to the code.

``` python
print('Calculation of a metal cubes weight')
print('-----------------------------------')

material = ['gold','silver','aluminium']
dens = [19.3, 10.5, 2.7]

print('- Materials -')
for i in material:
	print(i)

a = input('cube side length [cm]:')
a = int(a)
v = a*a*a

n = len(material)
index = 0
while index<n:
	mat = material[index]
	d = dens[index]
	weight = d*v
	print(mat,'... weight:',weight,'g')
	index = index+1
print('end of programm')
```

---------------------------------------

### Solution

``` python
print('Calculation of a metal cubes weight')
print('-----------------------------------')

material = ['gold','silver','aluminium']   # list of materials
dens = [19.3, 10.5, 2.7]                   # list of material density values

print('- Materials -')
for i in material:                         # print all materials
	print(i)

a = input('cube side length [cm]:')
a = int(a)
v = a*a*a                                  # calculate volume of the cube

n = len(material)                          # n: number of different materials
index = 0                                  # i: list access index
while index<n:                             # loop of all list items
	mat = material[index]                  #    get the material name
	d = dens[index]                        #    get the material density
	weight = d*v                           #    calculate the cubes weight
	print(mat,'... weight:',weight,'g')    #    print the result
	index = index+1                        #    increment index
print('end of programm')
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| basic list data structure operations           | worked-out example | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data types, calculations
loop-1: while-loop  
list-1: list and index, for-iteration
  
#### Learning Activities

1) read the code
2) run and understand the programm 
3) write comments to the code

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
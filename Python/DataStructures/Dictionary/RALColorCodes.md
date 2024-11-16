### Learning Task: RAL color codes

RAL is the most popular Central European color standard used today (https://www.ralcolor.com/). 
For example RAL 1013 is used as color code for the color Oyster white.

Implement a Python program that uses a dictionary to store the color name to be accessed by the related RAL color code.
The user shall enter multiple color names and the RAL codes and the program shall store this information in the dictionary.
In case the user does not enter a color code, the program will leave the loop and shall print an alphabetically sorted list of all RAL codes and the related colors.

Write this Python program, test it and explain it to another student.

---------------------------------------
---------------------------------------

##### Solution

``` python
# --- RAL colors ----

ral_colors = {}                      # dictionary to store the color data (key: RALcode value: color name)

while True:                          # loop to enter data
	ral = input('RAL code: ')        # enter RAL color code
	if ral == '':                    # no input:
		break                        #     break loop
	color = input('Color name: ')    # enter color name
	
	ral_colors[ral] = color          # store color name under RAL color code in the dictionary

# print sorted RAL codes and related color names	
ral_sort = sorted(ral_colors.keys()) # get a sorted list of dictionary keys
for r in ral_sort:                   # iterate all RAL codes
	print(r, '-', ral_colors[r])     # print RAL code and color name
```

##### Previous Knowledge

- basics of dictionaries
- basics of loops and branches
  
##### Learning Activities

1) read and understand the given task
2) define dictionary data structure
2) implement the Python code
3) test the written code
4) add comments to the code
5) explain the code to another student

##### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 120-125

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Dictionary data structures 

*Learning objective:*  
- store and access data using a dictionary

[//]: # "learning objective: 2-dictionary"
[//]: # "previous knowledge: 2-dictionary 2-loop 1-branch"

*Complexity:*  2-normal 

*Task type:*  conventional task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0
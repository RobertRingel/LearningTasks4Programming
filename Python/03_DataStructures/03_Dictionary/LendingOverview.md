Topic: data structures - dictionary

## Learning Task: Lending overview

The below Python program is used to manage lending personal items to other people. A dictionary data structure stores item names and the related lending information such as name and date.
The program prints an overview of the lended items and it can be used to lend other items or to remove them from the dictionary in case you get them back.

Read the Python code and get an understanding. Complete the missing dictionary statements. Finally run and test the program.

Compare your result with another student.

``` python
# --- my lending overview ----

lendings = {'PowerBank' : ('Frank','12.10.2024'), 
	        'DVD' : ('Liz','10.10.2024'),
   		    'novel' : ('Sue','11.09.2024') }

objects = ...                     # reference to dictionary keys

while True:
	print('\n--- lent objects ---')
	for o in sorted(objects):
		print(o)

	obj_key = input('Which object - or end to end the program? ')
	if obj_key == 'end':
		break
	object_data = ...             # access object data
	if object_data == None:
		d = input('Do want to lend it (y/n):')
		if d == 'y':
			name = input('To which person: ')
			date = input('Todays date: ')
			# store name and date information to the related object in the dictionary
			...
	else:
		print( ... )             # print object and related lending information
		r = input('Was it returned (y/n):')
		if r == 'y':
			...                  # delete object in dictionary
```

---------------------------------------

### Solution

``` python
# --- my lending overview ----

lendings = {'PowerBank' : ('Frank','12.10.2024'), 
	        'DVD' : ('Liz','10.10.2024'),
   		    'novel' : ('Sue','11.09.2024') }

objects = lendings.keys()                     # reference to dictionary keys

while True:
	print('\n--- lent objects ---')
	for o in sorted(objects):
		print(o)

	obj_key = input('Which object - or end to end the program? ')
	if obj_key == 'end':
		break
	object_data = lendings.get(obj_key)       # access object data
	if object_data == None:
		d = input('Do want to lend it (y/n):')
		if d == 'y':
			name = input('To which person: ')
			date = input('Todays date: ')
			# store name and date information to the related object in the dictionary
			lendings[obj_key] = (name,date)
	else:
		print(obj_key, lendings.get(obj_key))  # print object and related lending information
		r = input('Was it returned (y/n):')
		if r == 'y':
			lendings.pop(obj_key)              # delete object in dictionary
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| practise various dictionary statements         | completion task | 3 - high       |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-else  
loop-2: while-break loop  
tuple-1: create tuple  
dict-1, dict-3: define dictionary, dictionary stores tuple, access dictionary data
  
#### Learning Activities

1) read Python code
2) write specific dictionary statements
3) run and test the program
4) compare the final code with another student

#### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 120-125

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

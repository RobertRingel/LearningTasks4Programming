Topic: data structures - dictionary

## Learning Task: Product inventory

Read the given Python code and complete it. Understand the given part of the code and write comments to the indicated spots. 
Write the implementation of the else-part to print the requested inventory information for the product requested by the user input 
or print an error message in case the product is not listed in the shop.

Compare your result with another student.

``` python
# --- product inventory ----
# product : [ price, pieces, limit ]

inventory = {'beer' : [0.95, 250, 50], 
	         'wine' : [12.78, 45, 10],
   		     'butter' : [3.21, 324, 50] }

while True:
	print('\n--------------------------')
	for p in inventory.keys():                              # ... add your comment
		print(p)
	prod = input('Which product - enter name or all: ')
	if prod == 'end':
		break
	if prod == 'all':
		total = 0
		for key, value in inventory.items():                # ... add your comment
			price, pcs, limit = value[:]                    # ... add your comment
			print (key,':',pcs, 'pcs:', price,'EUR', pcs*price, 'EUR - limit:',limit)
			total = total + price*pcs
		print('total value:',total,'EUR')
	else:
		# IMPLEMENT: check if product is listed

		# IMPLEMENT: print product name, pieces, prices, price*piece and low storage limit
		
		# IMPLEMENT: or print a message in case the product is not listed
		
```

---------------------------------------

### Solution

``` python
# --- product inventory ----
# product : [ price, pieces, limit ]

inventory = {'beer' : [0.95, 250, 50], 
	         'wine' : [12.78, 45, 10],
   		     'butter' : [3.21, 324, 50] }

while True:
	print('\n--------------------------')
	for p in inventory.keys():                            # print a the product names by iterating all dictionary keys
		print(p)
	prod = input('Which product - enter name or all: ')
	if prod == 'end':
		break
	if prod == 'all':
		total = 0
		for key, value in inventory.items():              # iterate all dictionary items to get all product names (key) and product data (value)
			price, pcs, limit = value[:]                  # get detailled product information by extracting the data list into items
			print (key,':',pcs, 'pcs:', price,'EUR', pcs*price, 'EUR - limit:',limit)
			total = total + price*pcs
		print('total value:',total,'EUR')
	else:
		if prod in inventory.keys():                      # check if product is listed?
			item = inventory.get(prod)                    # yes: get the product data
			price, pcs, limit =  item[:]                  #      get detailled product information
			print(prod, ':', pcs ,'pcs:', price,'EUR', pcs*price, 'EUR - limit:',limit)  # print requested data
		else:
			print('unknown product')                      # print error message
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| access data stored in a dictionary             | completion task | 3 - high       |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-3: nested if-else  
loop-2: while-break  
list-2: list slicing  
dict-1, dict-2, dict-3: define dictionary, dictionary stores list, access dictionary data, iterate dictionary  
  
#### Learning Activities

1) reading Python code
2) write specific comments for dictionaries
3) write and test Python code for dictionary and list operations
4) run and test the implementation
5) explain the result to another student

#### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  Kapitel 4, Seiten 120-125

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025   
License: CC BY-SA 4.0

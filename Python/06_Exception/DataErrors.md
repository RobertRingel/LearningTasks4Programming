Topic: exceptions

## Learning Task: Handle data errors

The given Python program can be used to record atlethes results in a long jump competition.
Read the code and test the implementation by running the program. Note the different exception to be raised.  
Add comments to the code to describe the implemented exception handling.  
Add another exception to be raised in case the entered nation is not among the ones stored in the nations list.

``` python
# --- record competition data for long jump ---

def get_data():
	name = input('Name:')
	if name == 'END':
		return None

	nat = input('Nation:')		

	distance = -1.0
	try:
		distance = float(input('Distance [m]:'))
	except ValueError as verr:
		raise verr

	if distance>10.0:
		raise ValueError('Suspicious distance value:'+str(distance))

	record = (name,distance,nat)
	return record


results = []
nations = ['SUI','AUS','RSA','GER','CAN','FIN']

while True:
	try:
		record = get_data()
		if record == None:
			break	
		results.append(record)
	except Exception as err:
		print('There was a problem:', err)

print('---------------------------------------------------------------------')
print('All the data:')
print(results)
```

---------------------------------------

### Solution

``` python
# --- record competition data for long jump ---

def get_data():
	name = input('Name:')
	if name == 'END':
		return None

	nat = input('Nation:')		
	if nat not in nations:			               # check for registered nation
		raise RuntimeError('Unknown Nation:'+nat)  # trigger an error

	distance = -1.0
	try:                                           # cover risky type conversion
		distance = float(input('Distance [m]:'))
	except ValueError as verr:                     # catch the error
		raise verr                                 # forward it to function output

	if distance>10.0:                              # check for valid distance
		raise ValueError('Suspicious distance value:'+str(distance)) # trigger error

	record = (name,distance,nat)
	return record


results = []
nations = ['SUI','AUS','RSA','GER','CAN','FIN']

while True:
	try:                                           # secure data recording
		record = get_data()
		if record == None:
			break	
		results.append(record)
	except Exception as err:                       # catch errors
		print('There was a problem:', err)         # show error messages

print('---------------------------------------------------------------------')
print('All the data:')
print(results)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understand raising and handling exceptions     | completion task | 3 - high       |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-1: basic if  
loop-2: while-break loop  
list-1, list-3: basic list operations, list of tuples
tuple-1: tuple definition  
fun-1: basic function usage  
excp-1, excp-2: try-except, raise various exceptions

#### Learning Activities

1) read the given Python code
2) run the program in order to understand it  
3) write line comments to explain the code behaviour
4) add requested exception handling

#### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 5.6, Seiten 167-177

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
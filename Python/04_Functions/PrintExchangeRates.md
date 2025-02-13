Topic: functions

## Learning Task: Print exchange rates

Given is the following dictionary data structure:  
exchange_rates = {'GBP-USD':1.30, 'EUR-USD':1.09, 'USD-EUR':0.91, 'GBP-EUR':1.19, 'YEN-USD':0.0066}

Write a function that prints a simple sorted table of the exchange rates.  
Write a related function documentation in the Google-Doc-Style and implement a call to the function 
to demonstrate its functionality.

---------------------------------------

### Solution

``` python
exchange_rates = {'GBP-USD':1.30, 'EUR-USD':1.09, 'USD-EUR':0.91, 'GBP-EUR':1.19, 'YEN-USD':0.0066}

def print_rates_table(rates):
	"""
	Prints currency exchange rates in a simple sorted table format.

	Args:
		rates (dict): the rates as currencies : rate
	"""
	keys = sorted(rates.keys())
	for k in keys:
		print(k,':',rates[k])

print_rates_table(exchange_rates)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| function without return value                  | conventional task | 2 - normal     |  

#### Previous Knowledge

vcp-1: print, variable  
dict-1, dict-2: define dictionary, access dictionary data, for-iteration  
func-1: basic function call and implementation
  
#### Learning Activities

1) read and understand the given task and data structure
2) implement the function
3) implement a function call to test the function
4) write the function documentation

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
Topic: data structures - dictionary

## Learning Task: Currency rates

Read and run the given Python code in order to develop an understanding.  
Write comments to the lines of code.

Compare your result with another student and explain your understanding of a combined key for the dictionary.

``` python
# --- currency rates ----

rates = {'EUR-YEN':165.77, 'EUR-GBP':0.83} 

while True:
	print('\n--- Currency exchange rates ---')
	for c, r in rates.items():
		print(c,':',r)
	c1 = input('From currency: ')
	c2 = input('To currency:   ')
	if c1=='' or c2=='':
		break
	key = c1+'-'+c2
	r = rates.get(key)
	if r == None:
		val = float(input('rate: '))
		rates[key] = val
	else:
		print('Current rate: ',r)
		r = float(input('Enter new rate or <0.0 to keep it: '))
		if r > 0.0:
			rates[key] = r
print('Bye bye.')
```

---------------------------------------

### Solution

``` python
# --- currency rates ----

# dictionary {from-to : rate}
rates = {'EUR-YEN':165.77, 'EUR-GBP':0.83} 

while True:
	print('\n--- Currency exchange rates ---')
	for c, r in rates.items():                       # iterate entire dictionary to get all key-value pairs
		print(c,':',r)                               # print currencies and related rate
	c1 = input('From currency: ')                    # user enters source currency
	c2 = input('To currency:   ')                    # user enters destination currency
	if c1=='' or c2=='':                             # break loop in case one currency is not given
		break
	key = c1+'-'+c2                                  # construct key as concatenation of both currencies
	r = rates.get(key)                               # get related rate from dictionary
	if r == None:                                    # rate is not known 
		val = float(input('rate: '))                 #     enter new rate
		rates[key] = val                             #     store new rate in dictionary
	else:
		print('Current rate: ',r)                    # rate is known - print it
		r = float(input('Enter new rate or <0.0 to keep it: '))  # user can enter a new rate value
		if r > 0.0:
			rates[key] = r                                       # overwrite the current rate with the new one
print('Bye bye.')
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| access data in dictionary, concept of combined dictionary key | worked-out example | 3 - high       |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
str-1: string concatenation  
branch-2: if using or  
loop-2: while-break-loop  
dict-1, dict-2: access and store dictionary data, iterate all items  
  
#### Learning Activities

1) run, read and understand the given code
2) write comments to the code
3) explain the code to another student
4) explain the concept of a combined dictionary key

#### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 120-125

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

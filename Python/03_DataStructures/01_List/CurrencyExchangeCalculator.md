Topic: data structures - list

## Learning Task: Currency exchange calculation

The following program can be used to perform currency exchange calculations.

Read the program, run it and write comments to the code.  
Draw a documentation for the list data structure used by the code.

``` python
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

src = input('From what currency:')
dest = input('To what currency:')

i=0
while i<len(currencies):
	if src == currencies[i] and dest == currencies[i+1]:
		rate = currencies[i+2]
		amount = float(input('Amount:'))
		exchange = amount*rate
		print('You will get:',exchange,dest)
		break
	i=i+3

if i>=len(currencies):
	print('This is not possible.')
```

---------------------------------------

### Solution

``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

src = input('From what currency:')
dest = input('To what currency:')

i=0     # list index
# loop to loock up the required rate and to perform the calculation
while i<len(currencies):
	if src == currencies[i] and dest == currencies[i+1]:    # currencies found?
		rate = currencies[i+2]                              # yes: get rate
		amount = float(input('Amount:'))                    #      ask for amount
		exchange = amount*rate                              #      calc. exchange
		print('You will get:',exchange,dest)                #      print result
		break                                               #      break loop
	i=i+3                                                   # no:  increment index

if i>=len(currencies):                      # currencies not found
	print('This is not possible.')          #     print message
```

**Sketch of the list data structure:**

![](CurrencyExchangeCalculator.png)

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| access list items by index                     | worked-out example | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data types, calculations
loop-2: while-loop, break  
branch-2: if incl. conjunction
list-1: list and index

#### Learning Activities

1) read the Python code
2) get an understanding of the code
3) write comments to the code
4) draw a sketch of the data structure

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

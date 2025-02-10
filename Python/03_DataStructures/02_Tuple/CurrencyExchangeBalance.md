Topic:  data structures - tuple

## Learning Task: Currency exchange balance

The following program can be used to calculate the currency exchange balance out of the log of currency exchanges.  
Read and run the given code in order to get an understanding of the implementation. Then add comments to the code. 
Explain the tuple data structure as part of the comment!  
Finally explain your understanding to another student.

``` python
# --- currency exchange balance ---

exch = [('EUR','USD',450.00,488.62),('YEN','GBP',23000.00,117.87),('EUR','GBP',1200.00,999.30),('USD','EUR',342.00,315.01)]

currency = input('Which currency:')
sum_rec = 0.0
sum_spent = 0.0

for r in exch:
	src = r[0]
	dest = r[1]
	if src == currency:
		sum_rec = sum_rec + r[2]
	if dest == currency:
		sum_spent = sum_spent + r[3]

print('received:',sum_rec,'currency')
print('spent   :',sum_spent,'currency')
print('total   :',sum_rec-sum_spent,'currency')
```

---------------------------------------

### Solution

``` python
# list of performed currency exchanges - a tupel stores: (fromCurrency, toCurreny, fromAmount, toAmount)
exch = [('EUR','USD',450.00,488.62),('YEN','GBP',23000.00,117.87),('EUR','GBP',1200.00,999.30),('USD','EUR',342.00,315.01)]

currency = input('Which currency:')        # currency for balance to be calculated
sum_rec = 0.0                              # sum of received money
sum_spent = 0.0                            # sum of spent money

for r in exch:                             # iterate the entiere exchange log list
	src = r[0]                             # source currency
	dest = r[1]                            # destination currency
	if src == currency:                    # sum up for currency as source currency?
		sum_rec = sum_rec + r[2]           # yes: sum up received money
	if dest == currency:                   # sum up for currency as destination currency?
		sum_spent = sum_spent + r[3]       # yes: sum up spent money

# show balances
print('received:',sum_rec,'currency')
print('spent   :',sum_spent,'currency')
print('total   :',sum_rec-sum_spent,'currency')
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| access tuple data by index                     | worked-out example | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, calculations  
branch-1: simple if  
list-1: basic list, for-iteration  
tuple-1, tuple-2: define a tuple, list of tuples, index access  

#### Learning Activities

1) read and run the code in order to get an understandig of it
2) comment the structure of the tuple data structure
3) write comments to explain the code
4) explain the code to another student to validate the understanding

#### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 116-132

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

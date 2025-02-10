Topic: data structures - list

## Learning Task: Print a currency exchange rates table

The following list data structure can be used as a basis for a currency exchange calculation program.  

![](CurrencyExchangeCalculator.png)

Implement some lines of Python code to print a simple table of currency exchange rates as stored in the list.

``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

... complete the code here ...

```

---------------------------------------

### Solution

*Version 1*
``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

print('--- currency exhange rates ---')

i=0                                # list index variable
print('from','to','rate')
while i<len(currencies):           # loop over currencies
	record = currencies[i:i+3]     # extract a currency exch. record
	print(record)                  # print the record/sub-list
	i=i+3                          # increment the index
```

*Version 2*
``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

print('--- currency exhange rates ---')

i=0                                                         # list index variable
print('from','to','rate')
while i<len(currencies):                                    # loop over currencies
	print(currencies[i], currencies[i+1], currencies[i+2])  # print list items
	i=i+3                                                   # increment index
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| print data stored in a list data structure     | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1: print  
loop-1: while-loop  
list-2: list, index, slicing  

#### Learning Activities

1) get an understanding of the given list data structure
2) develop an idea to solve the problem 
3) write the code
4) test the code
5) write comments to the code

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

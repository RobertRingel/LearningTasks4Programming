### Learning Task: Remove currency exchange data

The following list data structure can be used as a basis for a currency exchange calculation program.  

![](CurrencyExchangeCalculator.png)

Implement some lines of Python code to remove the source currency, the destination currency and the exchange rate for an existing currency exchange.  
Finally print the updated list of currencies.

``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

... complete the code here ...

```

---------------------------------------
---------------------------------------

##### Solution

``` python
# data of currencies and rates
currencies = ['EUR','USD',1.12,'USD','EUR',0.91,'YEN','GBP',0.0051]

print('--- Remove currency exhange data ---')

src = input('source currency:')
dest = input('destination currency:')

src_idx = currencies.index(src)                         # get the source curr. index
if src_idx >= 0 and dest == currencies[src_idx+1]:      # check the dest. currency
	currencies.pop(src_idx)                             # delete source currency
	currencies.pop(src_idx)                             # delete destination currency
	currencies.pop(src_idx)                             # delete exchange rate
	print(currencies)
else:
	print(src,'is not a source currency.')

```

##### Previous Knowledge

- basic list operations
- index list operations
- branches
  
##### Learning Activities

1) get an understanding of the given list data structure
2) develop an idea to solve the problem 
3) write the code
4) test the code
5) write comments to the code

###### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 109-116

----
[//]: # "Learning objective: update data in an existing list data structure"
[//]: # "Topic: List data structures"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: completion task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0

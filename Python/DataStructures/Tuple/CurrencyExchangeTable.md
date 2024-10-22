### Learning Task: Currency exchange table

Implement a Python program that prints a currency exchange table.
The current exchange rates shall be stored in a list of tuples structured like (source_currency, destination_currency, rate).
Use tuple extraction to extract all data from the tuple in just one line of Python code.

Design, implement and test the program - explain the final program to another student.

``` python
# --- currency exchange table ---

# data of currencies and rates
currencies = [('EUR','USD',1.12,),('USD','EUR',0.91),('YEN','GBP',0.0051)]


...

```

---------------------------------------
---------------------------------------

##### Solution

``` python
# --- currency exchange table ---

# data of currencies and rates
currencies = [('EUR','USD',1.12,),('USD','EUR',0.91),('YEN','GBP',0.0051)]

print('--- currency exhange rates ---')

print('from','to','rate')
for record in currencies:
	source, dest, rate = record
	print(source,dest,rate)
```

##### Previous Knowledge

- basics about tuple and list data structures
  
##### Learning Activities

1) read and understand the given task
2) develop and implement the code
3) test the code 
4) explain the code to another student

##### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 116-132

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Tuple data structures 

*Learning objective:*  
- extract data from tuples in just one line of code

[//]: # "learning objective: 2-tuple"
[//]: # "previous knowledge: 3-list 1-tuple"

*Complexity:*  2-normal 

*Task type:*  conventional task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0

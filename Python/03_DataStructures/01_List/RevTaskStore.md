Topic: data structures - list

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
store = ['beer', 100, 0.76, 'wine',20, 5.10, 'gin', 2, 18.99]

total = 0
i=0
while i<len(store):
	prod = store[i]
	pieces = store[i+1]
	price = store[i+2]
	value = price*pieces
	total = total + value
	print(prod,':',pieces,'pcs',price,'EUR',value,'EUR')
	i = i+3

print('Total store value:',total,'EUR')
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the individual store item values as well as the overall store value.

*Programming task*  
Write a Python program to calculate the value of a store. The program shall print all store items, the number of pieces, the price and the resulting value.  
Finally the program shall print the overall store value.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| list item access by index                      | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1: print, variable  
loop-1: while-loop  
list-1: list and index
  
#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

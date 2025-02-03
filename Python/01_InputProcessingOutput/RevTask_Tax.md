Topic: variables, calculations, printing

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
TAX_RATE = 19/100
price = float(input('real price [EUR]:'))
tax = TAX_RATE*price/(1+TAX_RATE)
print('assumed VAT:',int(TAX_RATE*100),'%')
print('real price included VAT:',tax,'EUR')
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the value added tax, that is included in a given product price.

*Programming task*  
Write a Python program to calculate the value added tax, that is included in a given product price.
The user shall enter the product price and the programm shall print the included tax. The VAT is assumed to be 19%.

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding of variables, calculation and result printing | reverse task | 1 - low |  

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: input statement, float and int type conversion functions

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

[tutorialspoint.com: Assignments/Calculations](https://www.tutorialspoint.com/python/python_assignment_operators.htm)  
[tutorialspoint.com: User input](https://www.tutorialspoint.com/python/python_user_input.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

[www.python-kurs.eu: Ausdrücke und Operatoren](https://www.python-kurs.eu/python3_operatoren.php)

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:
Kapitel 2, Seiten 23-27 und Kapitel 3, Seiten 37-39

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
Lizenz: CC BY-SA 4.0

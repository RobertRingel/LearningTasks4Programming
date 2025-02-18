Topic:  exceptions

## Learning Task: Body-mass-index basic error handling

Read the given Python code and test the implementation by running the program.  
Make notes to explain the program behaviour in case of incorrect user input.

``` python
# Calculation of the body-mass-index

try:
	weight = int(input('Your weight [kg]:'))
	height = float(input('Your height [m]:'))
except:
	print('Illegal input - your input was not a number')
else:
	bmi = weight/height**2
	print('Your bmi:',bmi)
```

---------------------------------------

### Solution

**Notes regarding the program behaviour**  
- try-except is used to prevent the program to crash in case the user does not enter a number  
- in case the weight input is not a number the error message will be shown immediately and the user will never be asked about the height input  
- using the else statement, the bmi calculation and print-out will only be performed in case of correct numeric input

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understand basic exception handling            | worked-out example | 1 - low        |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data types  
excp-X: xxxxxxxx
  
#### Learning Activities

1) read the given Python code
2) run the program in order to test it  
3) write notes to explain the code behaviour

#### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 5.6, Seiten 167-177

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
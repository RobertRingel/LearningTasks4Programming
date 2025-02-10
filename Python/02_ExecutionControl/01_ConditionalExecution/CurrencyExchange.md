Topic: controlling program execution - branch

## Learning Task: Currency exchange calculator

The following Python code can be used to perform currency exchange calculations.  

Read the code and run the code to get an understandig of it. Add the missing lines of Python commands to perform all potential currency exchange calculations for the given currencies.

Improve the indicated command in a way to prevent negative currency exchanges. 

``` python
# This is a simple currency exchange calculator

RATE_USD_2_EUR = 0.84
RATE_USD_2_YEN = 105.42
RATE_EUR_2_YEN = 125.91

currency1 = input('from [EUR, USD, YEN]:')
currency2 = input('to   [EUR, USD, YEN]:')
amount1 = float(input('              amount:'))

amount2 = -1.0

if currency1 == 'USD' and currency2 == 'EUR':
	amount2 = amount1 * RATE_USD_2_EUR
elif currency1 == 'EUR' and currency2 == 'USD':
	amount2 = amount1 / RATE_USD_2_EUR

if amount2 != -1.0:       # improve this command to prevent negative exchanges
	print()
	print(amount1, currency1, ' = ',amount2, currency2)
else:
	print('invalid user input')

```

---------------------------------------

### Solution

``` python
# This is a simple currency exchange calculator

RATE_USD_2_EUR = 0.84
RATE_USD_2_YEN = 105.42
RATE_EUR_2_YEN = 125.91

currency1 = input('from [EUR, USD, YEN]:')
currency2 = input('to   [EUR, USD, YEN]:')
amount1 = float(input('              amount:'))

amount2 = -1.0

if currency1 == 'USD' and currency2 == 'EUR':
	amount2 = amount1 * RATE_USD_2_EUR
elif currency1 == 'EUR' and currency2 == 'USD':
	amount2 = amount1 / RATE_USD_2_EUR
elif currency1 == 'USD' and currency2 == 'YEN':
	amount2 = amount1 * RATE_USD_2_YEN
elif currency1 == 'YEN' and currency2 == 'USD':
	amount2 = amount1 / RATE_USD_2_YEN
elif currency1 == 'EUR' and currency2 == 'YEN':
	amount2 = amount1 * RATE_EUR_2_YEN
elif currency1 == 'EUR' and currency2 == 'YEN':
	amount2 = amount1 / RATE_EUR_2_YEN

if amount2 >= 0.0:
	print()
	print(amount1, currency1, ' = ',amount2, currency2)
else:
	print('invalid user input')

```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| test and branch using if-elif                  | completion task | 1 - low        |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variables and calculations, string variables  
branch-2: if-elif-else-statement
  
#### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) extent the code by using elif-statements
4) run and test the final program

#### Supporting information

[tutorialspoint.com: if-else Statement](https://www.tutorialspoint.com/python/python_if_else.htm)  
[tutorialspoint.com: Logical Operators](https://www.tutorialspoint.com/python/python_logical_operators.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 5, pages 72-84  

[www.python-kurs.eu: Bedingte Anweisungen](https://python-kurs.eu/python3_bedingte_anweisungen.php)

Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 41-48

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

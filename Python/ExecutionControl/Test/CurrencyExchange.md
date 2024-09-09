### Learning Task: Currency exchange calculator

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
---------------------------------------

##### Solution

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

##### Previous Knowledge

- print, input, variables and calculations, string variables
- if-elif-else-statement
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) extent the code by using elif-statements
4) run and test the final program


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Test and branch using if-elif"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: complition task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

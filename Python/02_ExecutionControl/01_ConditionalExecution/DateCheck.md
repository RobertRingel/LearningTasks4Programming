Topic: controlling program execution - branch

## Learning Task: Check the Date

The following Python code can be used to perform a basic date check.  

Read the code and complete the code in order to set the missing text messages and to initialize the date_check variable correctly.

Finally do not forget to run and test the program.

``` python
MIN_YEAR = 2024
MAX_YEAR = 2050

year = int(input('Enter year:'))
month = int(input('Enter month as number:'))
day = int(input('Enter day as number:'))

valid_year = year>=MIN_YEAR and year<=MAX_YEAR
valid_month = month>0 and month<13
valid_day = day>0 and day<32

message = ''
date_check = ...
if valid_year == False:
	message = 'Invalid year.'
elif valid...

...

else:
	date_check = True

print('Result for date check:', date_check)
print(message)
```

---------------------------------------

### Solution

``` python
MIN_YEAR = 2024
MAX_YEAR = 2050

year = int(input('Enter year:'))
month = int(input('Enter month as number:'))
day = int(input('Enter day as number:'))

valid_year = year>=MIN_YEAR and year<=MAX_YEAR
valid_month = month>0 and month<13
valid_day = day>0 and day<32

message = ''
date_check = False

if valid_year == False:
	message = 'Invalid year.'
elif valid_month == False:
	message = 'Invalid month'
elif valid_day == False:
	message = 'Invalid day'
else:
	date_check = True

print('Result for date check:', date_check)
print(message)
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| test and branch using if-elif                  | completion task | 1 - low        |  

#### Previous Knowledge

vcp-1, vcp-2: variables incl. string, calculations, print, type conversion for numeric input  
branch-2: if-elif-else-statements

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
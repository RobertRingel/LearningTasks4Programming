Topic: variables, calculations, printing

## Learning Task: Refund for Bottle Deposits

The following program calculates the refund for bottle deposits.  

Read the code and run the program.

Extend the code to include refund for can deposit of 25 cent per can.

``` python
# deposit per unit in Euro
PLASTIC = 0.25
GLASS = 0.08

glass_bottles = int(input('Count of glass bottles:'))
plastic_bottles = int(input('Count of plastic bottles:'))

refund = GLASS*glass_bottles + PLASTIC*plastic_bottles

print('Your total refund is:', refund, 'Euro')
```

Add-on task: Do you see any problem in the given code, in terms of stupid user input?

---------------------------------------

### Solution

``` python
# deposit per unit in Euro
PLASTIC = 0.25
GLASS = 0.08
CAN = 0.25

glass_bottles = int(input('Count of glass bottles:'))
plastic_bottles = int(input('Count of plastic bottles:'))
metal_cans = int(input('Count of metal cans:'))

refund = GLASS*glass_bottles + PLASTIC*plastic_bottles + CAN*metal_cans

print('Your total refund is:', refund, 'Euro')
```

Add-on: The program is not able to reject a negative number as invalid input. Therefore the if-statement is required as a new coding feature.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understanding variables, calculation and result printing | completion task | 1 - low  |

#### Previous Knowledge

vcp-1: print statement, variables and assignments to variables  
vcp-2: type conversion for numeric input  
  
#### Learning Activities

1) read and run the Python code
2) obtain an understanding of the code
3) extent the code by using the same coding pattern as in the given code
4) run and test the extended program

#### Supporting information

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
License: CC BY-SA 4.0

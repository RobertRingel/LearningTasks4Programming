### Learning Task: Refund for Bottle Deposits

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
---------------------------------------

##### Solution

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

##### Previous Knowledge

- print statement
- variables and assignments to variables
- type conversion for numeric input 
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) extent the code by using the same coding pattern as in the given code
4) run and test the extended program


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Understanding of variables, calculation and result printing"
[//]: # "Topic: variables, calculations, printing"
[//]: # "Complexity: 1 - low"
[//]: # "Task type: complition task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

### Learning Task: Bottle Deposit

The following program calculates the refund for bottle deposits.  

Read the code and run the program.

Extend the code to prevent the program to perform invalid calculations in case of invalid user input.
There are different valid solution approaches possible. Discuss them with another student before you start coding.
Try to find a solution that is valid using just one if-statement.

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

if (glass_bottles>=0) and (plastic_bottles>=0) and (metal_cans>=0):
	refund = GLASS*glass_bottles + PLASTIC*plastic_bottles + CAN*metal_cans
	print('Your total refund is:', refund, 'Euro')
else:
	print('Invalid user input')
```



##### Previous Knowledge

- print, input, variable, calculations
- if-else-statement
- and-conjunction of different comparisons
  
##### Learning Activities

1) read and run the Python code
2) get an understanding of the code
3) discuss and decide for a propper solution approach
4) extent the code by using an if statement to check different conditions
5) run and test the extended program


###### Supporting information

Seiten im THEIß-Buch  
[tutorialspoint.com: Variables](https://www.tutorialspoint.com/python/python_variables.htm)

----
[//]: # "Learning objective: Test and branch using if-else in combination with and-conjunction"
[//]: # "Topic: Controlling program execution"
[//]: # "Complexity: 2 - standard"
[//]: # "Task type: complition task"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 08/2024            
Lizenz: CC BY-SA 4.0

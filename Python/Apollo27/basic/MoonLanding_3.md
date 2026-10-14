Topic: Calculate, print, input

## Learn about branching program code 

if compares values and reacts accordingly. If the condition is met, the following commands are executed. These commands are indented by four spaces as a command block!  
```
if g <= 1: 
    print("Invalid input!")
```
else after if contains commands to become executed when the if condition is not satisfied:  
```
if g > 1: 
    v = g * t * 3.6
    s = 0.5 * g * t * t 
else: 
    print("Invalid input!")
```    
--- 
Type the program into the computer and run it!

``` python
# -----------
# Variant 3: Learning goal – if-else-branching
# -----------
print(">>> Moon Landing: Free Fall <<< ") 
t = 10
g = input("Gravitational acceleration [m/s²]: ") 
g = float(g) 

if g > 1: 
    v = g * t * 3.6             # falling velocity [km/h]
    s = 0.5 * g * t * t         # fallen distance [m] 
    print("Speed:", v, "km/h") 
    print("Distance:", s, "m") 
else:
    print("Invalid input!")

print("Program end.")
```

**Important notes about if statements**  

The if-line and the else-line always end with a colon :  
The else-clause is optional and does not have to be included.  

Multiple comparisons using and / or:  
... and ... both comparisons must be true  
... or ... it is sufficient if one of the comparisons is true  

Possible comparisons:  
< less than  
<= less than or equal to  
== equal to  
\> greater than  
\>=   greater than or equal to  
!=   not equal to

What is different in this variant of the program?
Type in the change and test the program!

``` python
# -----------
# Variant 3: Learning goal – if-else-branching
# -----------
print(">>> Moon Landing: Free Fall <<< ") 

t = input("Fall duration [s]: ")
t = int(t)

g = input("Gravitational acceleration [m/s²]: ") 
g = float(g) 

if g > 1 and t >= 1: 
    v = g * t * 3.6             # falling velocity [km/h]
    s = 0.5 * g * t * t         # fallen distance [m] 
    print("Speed:", v, "km/h") 
    print("Distance:", s, "m") 
else:
    print("Invalid input!")

print("Program end.")
```

### Potential learning tasks:

Run the program with different input values for fall duration on Earth and the Moon. Verify the results using a manual calculation on your calculator!

Explain the program to anybody else.

Add more comments to the code.

Describe the program functionality in 5-10 sentences.

---------------------------------------

##### Previous Knowledge

- print, variable, calculations ([vcp-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- type conversion for numeric input ([vcp-2:](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))  
- if-elif-else-statement ([branch-1:](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  


##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

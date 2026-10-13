Topic: Calculate, print, input

## Learn about keyboard input

input passes user input to a variable:  
name = input("What is your name?")  

Every input from an input-statement is text. In case a number is to be entered for calculations, it must be explicitly converted to the desired numeric type.  
t = input("Fall time [s]:")  
t = int(t)  

g = input("Gravitational acceleration [m/s²]:")  
g = float(g)  

int ... conversion to integer  
float ... conversion to floating-point number  

--- 
The Python program calculates the speed of a solid after a certain fall time and gravitational acceleration. Fall time and gravitational acceleration are entered using the keyboard.  

Type the program into the computer and run it!

``` python
# -----------
# Variant 2: Learning goal – variables, input, calculations, printing
# -----------

print(">>> Moon Landing: Free Fall <<<")

g = input("Gravitational acceleration [m/s2]: ")
g = float(g)

t = input("Fall time [s]: ")
t = int(t)

v = g * t * 3.6     # falling velocity [km/h]
s = 0.5 * g * t*t   # # fallen distance [m]

print("Velocity:",v,"km/h")
print("Distance:",s,"m")
```
**Note:**  
Gravitational acceleration at the Earth's surface: 9.81  
Gravitational acceleration at the Moon's surface: 1.622  

In case everything is implemented correctly, the program output should be:  
``` code
>>> Moon Landing: Free Fall <<<
Gravitational acceleration [m/s2]: 9.81
Fall time [s]: 10
Velocity: 353.16 km/h
Distance: 490.50000000000006 m
```

### Potential learning tasks:

Run the program with different input values for fall times on Earth and the Moon. Verify the results using a manual calculation on your calculator!

---------------------------------------

##### Previous Knowledge

- print, variable, calculations ([vcp-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- type conversion for numeric input ([vcp-2:](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

Topic: Calculate and print

## Learn about calculation and printing


print displays texts:  
print("Mission 1")  

Variables store values. To do this, an assignment is required:  
t = 10  
g = 1.662  

It is also possible to program an equation, and the calculation result is stored in the variable:  
v = g * t * 3.6

The values of the variables can be displayed using print:  
print("Velocity:", v, "km/h")  

--- 
The Python program calculates the speed of a solid after 10 seconds of fall time on the surface of the Moon.  
Type the program into the computer and run it!  
What result is displayed? Check the result by calculating it with a calculator!

``` python
# -----------
# Variant 1: Learning goal – variables, calculations, printing
# -----------

print(">>> Moon Landing: Free Fall <<<")
g = 1.622                     # Moon's gravitational acceleration [m/s²] 
t = 10                        # fall time [s] 
v = g * t * 3.6               # falling velocity [km/h]
print("Velocity:", v, "km/h")
```

**Note:** All text located after the # represents code comments to explain the program

### Potential learning tasks:
Extend the program to calculate and show the fallen distance. The distance shall be stored in a new variable s. It is calculated by the equation:  
s =  0.5 * g * t * t

In case everything is implemented correctly, the program output should be:  
``` code
>>> Moon Landing: Free Fall <<<
Velocity: 58.39200000000001 km/h
Distance: 81.10000000000001 m
```

Change the value of g to the Earth's gravitational acceleration g = 9.81 m/s². The program will the perform the calculation for free fall on Earth.

---------------------------------------

#### Solution

``` python
# -----------
# Variant 1: Learning goal – variables, calculations, printing
# -----------

print(">>> Moon Landing: Free Fall <<<")
g = 1.622                     # Moon's gravitational acceleration [m/s²] 
t = 10                        # fall time [s] 
v = g * t * 3.6               # falling velocity [km/h]
s =  0.5 * g * t * t          # fallen distance [m]
print("Velocity:", v, "km/h")
print("Distance:", s, "m")
```

---------------------------------------

##### Previous Knowledge

- print, variable, calculations ([vcp-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

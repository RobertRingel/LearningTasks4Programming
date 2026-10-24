Topic: Branches and loops

## Learn about loops to repeat code sections 

The while loop repeats commands as long as a comparison condition is true. All commands that need to be repeated by the while loop must be indented by four spaces.  
In the following example, the calculation and display are repeated as long as the value of h is greater than 0.0. In each loop iteration, the value of h is reduced by 100.0.  
```
h = 1000.0
while h > 0.0:
    print(h)
    h = h - 100.0
print("End of loop")
print(h)
```

We are going to apply the while loop in the following Python program. The program will simulate a free fall to the surface of the Moon in time steps (increments) of 1 second. This is the basis for later code development towards safe landing on the Moon with help of retrorockets.

--- 
Type the program into the computer and run it!

``` python
# ----------
# Variant 4: Learning objective: Loop/Repetition 
# ----------
print(">>> Moon Landing: Free fall <<<")
g = 1.622       # Moon gravity [m/s2]
h = 1000.0      # Initial altitude: 1000 m above the Moon 
s = 0.0         # Distance fallen [m]
v = 0.0         # Initial falling velocity: 0 m/s 
ds = 0          # Distance fallen in the current step [m] 
v0 = v
t = 0           # Elapsed time [s] 
dT = 1          # Time step increment: 1 s
a = g 

while h > 0.0: 
    print("t=", t, " a:", a, "s:", s, "h:", h, "v:", v, "ds:", ds)
    a = g                       # Acceleration without braking
    v0 = v                      # Previous velocity
    v = v + a * dT              # New velocity

    ds = 0.5 * a * dT * dT + v0 * dT  # Distance fallen in 1 second
    s = s + ds                  # Total distance fallen
    h = h - ds                  # Current altitude

    t = t + dT

print("Touch down ... survived?") 
v = 3.6 * v 
print("Impact velocity:", v, "km/h")
```

**Important notes about while statements**  

The while-line always ends with a colon :  


### Potential learning tasks:

Name the condition to be checked in order to repeat the while loop!  

Highlight all Python commands belonging to the loop!

Name the first command after the loop!

Add an input-statement to let the user enter the initial altitude.  

Do you have an idea how to add deceleration by retrorockets into the above program? If yes, explain them to another student and write appropriate comments into the code.  

---------------------------------------

#### Solution

``` python
# ----------
# Variant 4: Learning objective: Loop/Repetition 
# ----------
print(">>> Moon Landing: Free fall <<<")
g = 1.622       # Moon gravity [m/s2]
h = 1000.0      # Initial altitude: 1000 m above the Moon 
s = 0.0         # Distance fallen [m]
v = 0.0         # Initial falling velocity: 0 m/s 
ds = 0          # Distance fallen in the current step [m] 
v0 = v
t = 0           # Elapsed time [s] 
dT = 1          # Time step increment: 1 s
a = g 

while h > 0.0:  # head of the loop - will repeat as long as altitude is greater zero
    print("t=", t, " a:", a, "s:", s, "h:", h, "v:", v, "ds:", ds)
    # input to enter amount of fuel to burn fb by retrorockets
    # fuel = fuel - fb
    # calculate deceleration force b resulting from burned fuel
    # a = g - b  will replace the next line
    a = g                       # Acceleration without braking
    v0 = v                      # Previous velocity
    v = v + a * dT              # New velocity

    ds = 0.5 * a * dT * dT + v0 * dT  # Distance fallen in 1 second
    s = s + ds                  # Total distance fallen
    h = h - ds                  # Current altitude

    t = t + dT

print("Touch down ... survived?")      # first command after loop
v = 3.6 * v 
print("Impact velocity:", v, "km/h")
```

---------------------------------------

##### Previous Knowledge

- print, variable, calculations ([vcp-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- while-loop ([loop-1:](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md))  


##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

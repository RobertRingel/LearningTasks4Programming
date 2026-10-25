Topic: Functions

## Learning Task: Understand the idea of functions

Functions are pieces of code implemented to provide a specific service. In many cases they are used to perform certain calculations or to show certain data.
A function has a name and it may have one or more parameters. This is the purpose of the def-line.  
All function related code following the def-line must be indented by 4 spaces.  
The return-statement is used to return the function result.  

The example below implements a function to calculate the landing score depending on remaining fuel and touch down velocity.

```
def calc_LandingScore(velocity, rem_fuel):
    factor = 10.0
    if rem_fuel <= 0.0:
        return 0.0
    score = factor * rem_fuel / velocity
    return score
```
Note: Any variables that are defined within the function (variable factor in the above example) are only valid inside the function.  

To make use of a function you need to call it. The code below shows a call of the landing score calculation:  

```
print("Touch down.")
v = 3.6 * v
print("    ... speed:", v, "km/h")                  
scr = calc_LandingScore(v, f)           # function call
print("Landing score:", scr)
```

---  

The following Python program is a simulation of the landing on the Moon. It implements the landing [physics using retrorockets](../LandingPhysics.md).

Read the code and identify calculations to be implemented as Python functions!

``` python
# -----------
# Variant 6: Learning goal identify potential functions to be implemented
# -----------
def calc_LandingScore(velocity, rem_fuel):
    factor = 10.0
    if rem_fuel <= 0.0:
        return 0.0
    score = factor * rem_fuel / velocity
    return score

print(">>> Moon landing with braking: <<< ")
print("    task 6")
print()

g = 1.622     # Moon gravity (m/s²)
f = 1500.0    # Initial volume of braking fuel [kg]
fbr = 10.0    # Fuel burn rate per second [l/s]
h = 1000.0    # Initial altitude: 1000 m above the Moon
s = 0.0       # Total distance traveled (fall)
v = 0.0       # Initial falling velocity (m/s)
ds = 0.0      # Distance fallen in the current step [m]
v0 = v
b = 0.0       # Braking acceleration (m/s²)
t = 0.0       # Elapsed time [s]
dT = 1.0      # Time increment (1 s)

a = g
while h > 0.0:           # one loop per second until touch down
    print("t =", t, "   a:", a, " s:", s, " h:", h, " v:", v, " ds:", ds, end=" | ")

    fb = input("Braking fuel (0‑50): ")
    fb = int(fb)
    f = f - fb                  # Fuel consumption
    b = fb / (fbr*dT)           # Braking force derived from fuel
    a = g - b                   # Net acceleration after braking
    v0 = v                      # Previous velocity
    v = v + a*dT                # New velocity

    ds = 0.5 * a * dT * dT + v0 * dT   # Distance fallen in 1 s
    s = s + ds                         # Total fallen distance
    h = h - ds                         # Current altitude

    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        break

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v, "km/h")                  
scr = calc_LandingScore(v, f)           # function call
print("Landing score:", scr)
```

---------------------------------------

#### Solution

- calc_DecelForce: b = fb / (fbr*dT)  
- calc_FallDistance: ds = 0.5 * a * dT * dT + v0 * dT  
- calc_Velocity_kmh: v = 3.6 * v  

---------------------------------------

##### Previous Knowledge

- print, variable, input ([vcp-1, vcp-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- basic if ([branch-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  
- while-break loop ([loop-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md))  
- basic function call and implementation ([func-1](https://github.com/RobertRingel/LearningTasks4Programming/tree/main/Python/04_Functions))  

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

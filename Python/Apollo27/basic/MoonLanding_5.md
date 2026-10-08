Topic: Loops and Branches

## Learning Task: Understand and adapt the given Python program

The following Python program is a simulation of the landing on the Moon. It implements the landing [physics using retrorockets](../LandingPhysics.md).

Read and run the code. Discuss your understanding with another student. Solve one of the suggested learning tasks below or adapt the code as you like.

``` python
# -----------
# Variant 5: Learning goal – loop / repetition
# -----------

print(">>> Retrorockets Moon landing <<< ")
print("    task 5")
print()

g = 1.622     

h = 1000.0    
s = 0.0       
v = 0.0       
ds = 0.0      
v0 = v

b = 0.0       
t = 0.0       
dT = 1.0      
f = 1500.0    

a = g
while h > 0.0:    
    print("t =", t, "   a:", a, " s:", s, " h:", h, " v:", v, " ds:", ds)

    fb = input("Braking (0‑10): ")
    fb = int(fb)
    f = f - fb    
    b = fb / 10.0 
    a = g - b     
    v0 = v        
    v = v + a     

    ds = 0.5 * a * dT * dT + v0 * dT   
    s = s + ds                         
    h = h - ds                         

    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        break

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v*3.6, "km/h")

```
### Potential learning tasks:
- students shall write comments to the code  
- change the print-statement in a way to get the input right after the print-out and not at the next line  
- develop a a landing score depending on the touch-down speed and the remaining fuel  
- implement the landing score and print it at the very end of the program
- write a manual to explain the code and to describe a strategy to land safely

... identify potential improvements of the program!

---------------------------------------

#### Solution

``` python
# -----------
# Variant 5: Learning goal – loop / repetition with braking
# -----------

print(">>> Moon landing with braking: <<< ")
print("    task 5")
print()

g = 1.622     # Moon gravity (m/s²)

h = 1000.0    # Starting altitude: 1000 m above the Moon
s = 0.0       # Total distance traveled (fall)
v = 0.0       # Initial falling speed (m/s)
ds = 0.0      # Distance covered in the current step [m]
v0 = v

b = 0.0       # Braking acceleration (m/s²)
t = 0.0       # Elapsed time [s]
dT = 1.0      # Time increment (1 s)
f = 1500.0    # Amount of braking fuel [kg]

a = g
while h > 0.0:           # one loop per second until touch down
    print("t =", t, "   a:", a, " s:", s, " h:", h, " v:", v, " ds:", ds, end=" | ")

    fb = input("Braking (0‑10): ")
    fb = int(fb)
    f = f - fb                  # Fuel consumption
    b = fb / 10.0               # Braking force derived from fuel
    a = g - b                   # Net acceleration after braking
    v0 = v                      # Previous velocity
    v = v + a                   # New velocity

    ds = 0.5 * a * dT * dT + v0 * dT   # Distance fallen in 1 s
    s = s + ds                         # Total fallen distance
    h = h - ds                         # Current altitude

    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        break

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v*3.6, "km/h")                  
```

**Landing score:** should be maximized depending on remaining fuel and touch down velocity.
Velocity should be less the 5 km/h and fuel should be 500 kg or more. This would yield a score around 100 according to the basic equation of: score = f/v

---------------------------------------

##### Previous Knowledge

- print, variable, input ([vcp-1, vcp-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- basic if ([branch-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  
- while-break loop ([loop-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md)) 


##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

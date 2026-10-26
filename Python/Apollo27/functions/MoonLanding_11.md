Topic: Functions

## Learning Task: Implement functions

Implement the following two functions in the given Python code variant 6:

- calc_DecelForce: b = fb / (fbr*dT)  
- calc_FallDistance: ds = 0.5 * a * dT * dT + v0 * dT  

``` python
# -----------
# Variant 6: Learning goal function programming
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
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")
    fb = input("Braking fuel (0‑50): ")
    fb = int(fb)
    f = f - fb                  # Fuel consumption
    b = fb / (fbr*dT)           # Deceleration force derived from fuel
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

``` python
# -----------
# Variant 6: Learning goal function programming
# -----------

def calc_DecelForce(fuel_volume, duration, fuel_flow_rate):
    decel_force = fuel_volume / (duration * fuel_flow_rate)
    return decel_force


def calc_FallDistance(acceleration, velocity, duration):
    distance = 0.5 * acceleration * duration * duration + velocity * duration
    return distance


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
    f = f - fb                         # Fuel consumption
    b = calc_DecelForce(fb, dT, fbr)   # Deceleration force derived from fuel <<< function call
    a = g - b                          # Net acceleration after braking
    v0 = v                             # Previous velocity
    v = v + a*dT                       # New velocity

    ds = calc_FallDistance(a, v0, dT)  # Distance fallen in 1 s <<< function call
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

**Add-on task:**  

Implement a function to calculate the remaining fuel percentage based on the initial fuel value of 1500l.
Print the remaining fuel percent value after landing and if you like also as part of the variable print-line in every calculation loop.

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

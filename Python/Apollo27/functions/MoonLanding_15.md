Topic: Functions

## Learning Task: Modules are libraries of functions

Collections of functions related to a certain domain or task can be stored in one Python code file, a so called module. In order to use these functions by a Python program, the module file needs to be imported at the very begin of the Python program.  
Modules must be available at the same directory as the Python program or they must be located at the Python library path (e.g. PYTHONPATH environment variable).

The current version of the Apollo-27 Moon landing simulation (MoonLander_v14.py) provides the following functions:

```
calc_decel_force(fuel_volume, duration, fuel_flow_rate)  

calc_fall_distance(acceleration, velocity, duration)  

simulate_descent_step(gravity, braking_force, initial_velocity, altitude, time_step)  

calc_landing_score(velocity, rem_fuel)  

print_alt_indicator(altitude, distance_fallen, max_alt=1000.0)
```

We can consider all of the of generic nature for a Moon landing simulation except the "print_alt_indicator" that is a very specific altitude visualization. So we decide to move the function definition python code of the calc- and simulate-functions to the Python module file "lunar_physics_model.py". Consequently the Moon landing simulation needs to import this Python module to make use of it. The new Moon landing simulation MoonLander_v15.py is implemented as follows:

``` python
import lunar_physics_model as lpm

def print_alt_indicator(altitude, distance_fallen, max_alt=1000.0):
    """
    Print a visual altitude indicator showing the lander's position and descent.
    Uses a bar to represent altitude and a "falling" segment to show distance fallen.

    Args:
        altitude (float): Current altitude [m]
        distance_fallen (float): Distance fallen in this step [m]
        max_alt (float): Maximum altitude for scaling [m]
    """
    width = 80  # Width of the visual bar
    # Position of the lander in the bar (0 = bottom, width = top)
    pos = int(width * altitude / max_alt)

    # Scale distance fallen to fit in the bar (every 5m = 1 character)
    ds5 = int(distance_fallen / 5)
    # Limit to avoid overwriting the lander or going beyond the bar
    ds5 = min(ds5, width - pos - 1)

    # Build the visual bar: | + empty space + lander (<) + descent trail (-)
    line = "|" + " " * pos + "<" + "-" * ds5
    print(f"{line:<90}", end=".")


# -------------- main program --------------------------

print(">>> Moon landing with braking: <<< ")
print("    task 6")
print()

g = 1.622     # Moon gravity (m/s²)
f = 1500.0    # Initial volume of braking fuel [l]
fbr = 10.0    # Fuel burn rate per second [l/s]
h = 1000.0    # Initial altitude: 1000 m above the Moon
v = 0.0       # Initial falling velocity (m/s)
ds = 0.0      # Distance fallen in the current step [m]
b = 0.0       # Braking acceleration (m/s²)
t = 0.0       # Elapsed time [s]
dT = 1.0      # Time increment (1 s)

while h > 0.0:  # One loop per second until touch down
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")
    print_alt_indicator(h, ds)

    fb = input("Braking fuel (0–50): ")
    fb = int(fb)
    f = f - fb  # Fuel consumption

    b = lpm.calc_decel_force(fb, dT, fbr)
    v, h, ds = lpm.simulate_descent_step(g, b, v, h, dT)
    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        break

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v, "km/h")
scr = lpm.calc_landing_score(v, f)  
print("Landing score:", scr)
```

What are the benefits of such function modules?
1) A module is re-usable for different Python programs that need to make use of the module functions.
2) The program code of the main program is much shorter than before.


### Potential learning tasks


Change your Python program in the same way: implement the Python module lunar_physics_model.py and the main program MoonLander_v15.py as shown above.
Perform a test run to verify the program MoonLander_v15.py is running correctly.  

Implement a function to calculate the required amount of retro-rocket braking fuel as part of the module "lunar_physics_model.py".   

Implement a new version of the Moon landing simulation that makes use of above function instead of user input for braking fuel.


---------------------------------------


##### Previous Knowledge

- print, variable, input ([vcp-1, vcp-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- basic if ([branch-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  
- while-break loop ([loop-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md))  
- writing and using modules  ([func-3](https://github.com/RobertRingel/LearningTasks4Programming/tree/main/Python/04_Functions))  

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2026  
License: CC BY-SA 4.0

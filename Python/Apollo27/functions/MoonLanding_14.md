Topic: Functions

## Learning Task: Functions may return multiple values at once

A function return statement can have a comma-separated list of variables to be returned as the result of the function. The function calling statement will then make an assignment to different variables separated by commas. 

```
def enter_name_rank():
    """
    User will enter name and rank of the lunar mission commander.
    
    Returns:
        tuple containing
        - name: name of the commander.
        - rank: rank of the commander.

    """
    name = input("Commander's name:")
    rank = input("Commander's rank":)
    return name, rank


cmd_name, cmd_rank = enter_name_rank()

```

We can use this to implement a new function named 'simulateDescentStep' to calculate and update all landing physics variables at once.
The Python code below shows the implementation of this function.

``` python
def simulateDescentStep(gravity, braking_force, initial_velocity, altitude, time_step):
    """
    Simulate one time step of the descent.
    Applies net acceleration (gravity - braking) to update velocity and altitude.
    Args:
        gravity (float): Gravitational acceleration [m/s²]
        braking_force (float): Thrust-based deceleration [m/s²])
        initial_velocity (float): Velocity at start of time step [m/s]
        altitude (float): Current altitude [m]
        time_step (float): Duration of time step [s]
    Returns:
        tuple: (new_velocity, new_alt, distance_fallen)
    """
    # Net acceleration: gravity pulls down, braking force pushes up
    net_acceleration = gravity - braking_force

    # Update velocity using: v = v0 + a * t
    new_velocity = initial_velocity + net_acceleration * time_step

    # Calculate distance fallen during this time step
    distance_fallen = calc_FallDistance(net_acceleration, initial_velocity, time_step)

    # Update altitude
    new_altitude = altitude - distance_fallen

    return new_velocity, new_altitude, distance_fallen

...

while h > 0.0:           # one loop per second until touch down

    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")
    printAltIndicator(height, distance_fallen)

    fb = input("Braking fuel (0‑50): ")
    fb = int(fb)

    f = f - fb                                        # Fuel consumption
    b = calc_DecelForce(fb, dT, fbr)
    v, h, ds = simulateDescentStep(g, b, v, h, dT)
    t = t + dT

...
```

First: Add the new function 'simulateDescentStep' to your current code.  
Second Update the Python code below the while - loop accordingly.

### Potential learning tasks

Test and run the current version of the program.  
Make sure the documentation matches the actual code!  
Add some notes about functions returning a tuple of result values into your learning log.  

Check the code for potential improvements - note any findings on a separate sheet in your learning log.  

---------------------------------------


##### Previous Knowledge

- print, variable, input ([vcp-1, vcp-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- basic if ([branch-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  
- while-break loop ([loop-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md))  
- function call and multiple return values ([func-2](https://github.com/RobertRingel/LearningTasks4Programming/tree/main/Python/04_Functions))  

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2026  
License: CC BY-SA 4.0

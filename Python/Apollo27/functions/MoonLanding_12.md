Topic: Functions

## Learning Task: Write function code documentation

Functions need to have a documentation because the are re-usable elements of programs. Other programmers will read the function documentation before they read the code itself. Therefore the function documentation must fit to the function implementation.

A very popular style of function documentation is Google Docstring Style that follows this strict layout:  

```
def function_name(param1, param2):
    """
    One-line summary of what the function does.
    
    Extended description of the function's purpose, behavior, and any important details.
    
    Args:
        param1 (type): Description of parameter 1.
        param2 (type): Description of parameter 2.
    
    Returns:
        return_type: Description of what is returned.
    """
```

The challenge of writing function documentation is being correct and brief at once. This needs practice!  
See the function documentation for calculating the landing score.

``` python
# -----------
# Variant 6: Learning goal function programming
# -----------
def calc_LandingScore(velocity, rem_fuel):
    """
    Calculate a landing score based on the final velocity and remaining fuel.
    The score is proportional to remaining fuel and inversely proportional to velocity.
    If no fuel remains, the score is zero.

    Args:
        velocity (float): Final landing velocity [m/s]
        rem_fuel (float): Remaining fuel after landing [kg]

    Returns:
        float: Landing score (higher is better). Returns 0.0 if no fuel remains.
    """
    factor = 10.0
    if rem_fuel <= 0.0:
        return 0.0
    score = factor * rem_fuel / velocity
    return score
```

Write a similar documentation for the functions calc_DecelForce and calc_FallDistance!

``` python

def calc_FallDistance(acceleration, velocity, duration):
    distance = 0.5 * acceleration * duration * duration + velocity * duration
    return distance


def calc_LandingScore(velocity, rem_fuel):
    factor = 10.0
    if rem_fuel <= 0.0:
        return 0.0
    score = factor * rem_fuel / velocity
    return score
```

### Potential learning tasks

Cross review your own documentation and the one of another student.  

Make sure the documentation matches the actual code!

---------------------------------------

#### Solution

``` python
def calc_DecelForce(fuel_volume, duration, fuel_flow_rate):
    """
    Calculate the deceleration force [m/s²] produced by burning a given volume of fuel
    over a specified duration at a given fuel flow rate.

    Args:
        fuel_volume (float): Volume of fuel burned in the current time step [l]
        duration (float): Duration of the burn [s]
        fuel_flow_rate (float): Fuel burn rate [l/s]

    Returns:
        float: Deceleration force [m/s²] produced by the fuel burn
    """
    decel_force = fuel_volume / (duration * fuel_flow_rate)
    return decel_force


def calc_FallDistance(acceleration, velocity, duration):
    """
    Calculate the distance fallen during a time interval given initial velocity and constant
    acceleration (e.g., net gravity minus braking).

    Args:
        acceleration (float): Net acceleration acting on the spacecraft [m/s²]
        velocity (float): Initial velocity at the start of the time interval [m/s]
        duration (float): Time interval over which the motion occurs [s]

    Returns:
        float: Distance fallen during the time interval [m]
    """
    distance = 0.5 * acceleration * duration * duration + velocity * duration
    return distance
```

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

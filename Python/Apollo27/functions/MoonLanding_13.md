Topic: Functions

## Learning Task: No-return function

There are a few more things to know about functions. You can implement functions in order to do a certain job but not to return a calculation result. Such functions can be used to just print a bunch of information. A function like this would end by the last statement of the function code - without any return. Or it will be performed until it hits a return statement. But in that case the return statement will have no return value or variable - just a blank return.

```
def print_beginner_info(experience):
    if experience < 50:
        print("A lot of important notes for you ...")
        return 
    print("You are an expert - enjoy landing on the Moon!")
```

The following function prints an altitude indicator for the Apollo-27 simulation. It will print a "<" character to indicate the altitude above lunar surface. To right side of the "<" it will print a row of "-" characters to indicate the fallen distance (similar to velocity). So the user will get a visual impression of the landing approach.

The key feature of the implementation is the Python star-operation for strings. It does repeat a given string as often as stated by the star-operation.
Try the following Python commands as demo program:

```
alt = 7                    # assumed altitude
fall_dist = 3              # assumed fall_dist

# create visual string representation for altitude and fall_dist
alt_str = " " * alt                 # would be "       "
fall_dist_str = "-" * fall_dist     # would be "---"

display = "|" + alt_str + "<" + fall_dist_str   
print(display)                      # should print "|       <---"
```

Do you understand the idea of printing the altitude indicator display?  
Adopt the code to play a little around and talk to another student about it.  
You need to have understood it before proceeding with the given function below.

---  

Next you see a complete implementation of the altitude indicator. It uses a default value of 1000 meters for the maximum altitude.
Type the code of this function into thew current version of the Apollo-27 Python program. 

``` python
def printAltIndicator(altitude, distance_fallen, MAX_ALT=1000):
    """
    Print a visual altitude indicator showing the lander's position and descent.
    Uses a bar to represent altitude and a "falling" segment to show distance fallen.
    Args:
        altitude (float): Current altitude [m]
        distance_fallen (float): Distance fallen in this step [m]
        MAX_ALT (float): Maximum attitude for scaling [m]
    """
    WIDTH = 80  # Width of the visual bar
    # Position of the lander in the bar (0 = bottom, WIDTH = top)
    pos = int(WIDTH * altitude / MAX_ALT)

    # Scale distance fallen to fit in the bar (every 5m = 1 character)
    ds5 = int(distance_fallen / 5)
    # Limit to avoid overwriting the lander or going beyond the bar
    ds5 = min(ds5, WIDTH - pos - 1)

    # Build the visual bar: | + empty space + lander (<) + descent trail (-)
    line = "|" + " "*pos + "<" + "-"*ds5
    print(f"{line:<90}", end=".")
```

In order to make use of this function you need to at a call to the function. Implement the function call as follows:

``` python
while h > 0.0: 
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")
    printAltIndicator(height, distance_fallen)

    fb = input("Braking fuel (0‑50): ")
    fb = int(fb)
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

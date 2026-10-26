Topic: Calculate, print, input

## Learn about formatting print output

Often it is very beneficial to align print-output left, right, centered or to limit the number of printed decimals.
In Python printing so-called **f-Strings** provide this functionality.
``` 
altitude = 142.0121
print(f"Alt: {altitude:>6.1f}m") 
``` 
... will print: 
```
Alt:  142.0m
```

It shows the text "Alt:" and the value of the variable altitude followed by "m". But the variable value is shown right-aligned of 6 characters, 1 decimal as fix-point format (decimal is always shown).
 
You can use **<** for left alignment or **^** for centered print-out.  
Beside **f** for fix-point format **g** is used to request general format to suppress trailing zeros or use **e** to get scientific format.


So we can change the variable print-out as follows to get a much nicer result in the Moon landing program:  
``` python
print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ")
```

Add this line into the Python code right below the while-line and remove the current print-line from the code.
``` python
while h > 0.0:   
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ")
```

Run the adapted Python program and watch the new printings!

**Note:** You can add an **end=':'** as parameter to the print statement. In that case the print will not produce a line break but it will end with the given character.  
Try the following print statement right below the while loop:  
``` python
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end='|')
```
Do you see the effect?


Add some notes about the f-String options to your learning reflection sheets.

---------------------------------------

##### Previous Knowledge

- print, variable, calculations ([vcp-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))
- type conversion for numeric input ([vcp-2](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/01_InputProcessingOutput/00_TaskPool_InputProcessingOutput.md))  
- if-elif-else-statement ([branch-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/01_ConditionalExecution/00_TaskPool_ConditionalExecution.md))  
- while-loop ([loop-1](https://github.com/RobertRingel/LearningTasks4Programming/blob/main/Python/02_ExecutionControl/02_Loop/00_TaskPool_Loop.md))  

##### Supporting information

[Python Cheat Sheet: https://static.realpython.com/python-cheatsheet.pdf](https://static.realpython.com/python-cheatsheet.pdf)

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0

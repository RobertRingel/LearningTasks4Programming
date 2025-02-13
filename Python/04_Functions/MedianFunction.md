Topic: functions

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?
Write the text for a related programming task.

Finally feel free to write comments to the code.

``` python
def median(values):
    """
    Calculates the median of a list of numbers.

        Args:
            values (list) : a list of int or float numbers

        Returns:
            int or float : the median value
    """
    med_val = None
    srt_data = sorted(values)
    n = len(values)
    if n%2 == 1:               
        med_idx = int(n/2)            
        med_val = srt_data[med_idx]
    else:                                       
        m = int(n/2)-1                          
        med_val = (srt_data[m]+srt_data[m+1])/2 
    return med_val

# --- main part ---
numbers = [1, 34, 7, 12, 17]
med = median(numbers)
print(med)

numbers.pop(0)
med = median(numbers)
print(med)
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the median of a series of numbers using an appropriate calculation function.

*Programming task*  
Write a Python function to calculate the median of a list of integer numbers. Demonstrate the function call 
for a list storing an odd number of values and for another list that has an even number of values.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| write a function implementation                | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, variable, data type  
branch-2: if-else  
list-1: access define a list, items by index  
func-1: basic function call and implementation

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
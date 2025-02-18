Topic: exceptions

## Learning Task: Body-mass-index multiple error handlings

Read the given Python code and test the implementation by running the program.  
Add comments to the code to describe the implemented exception handling.
Explain your understanding to another student.

``` python
# Calculation of the body-mass-index

try:
    weight = int(input('Your weight [kg]:'))
    height = float(input('Your height [m]:'))
    bmi = weight/height**2
    if bmi < 0.0:
        raise RunTimeError('Negative result is invalid!')
    print('Your bmi:',bmi)
except ValueError:
    print('Illegal input - your input was not a number')
except RunTimeError as err:
    print('Error:', err)
```

---------------------------------------

### Solution

``` python
# Calculation of the body-mass-index

try:                               # begin of a risky section
    weight = int(input('Your weight [kg]:'))
    height = float(input('Your height [m]:'))
    bmi = weight/height**2
    if bmi < 0.0:                  # negative BMI -> raise error
        raise RunTimeError('Negative result is invalid!')
    print('Your bmi:',bmi)
except ValueError:                 # handle ValueError caused by type conversion
    print('Illegal input - your input was not a number')
except RunTimeError as err:        # handle RuntimeError caused by negative BMI
    print('Error:', err)
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understand raising and handling exceptions     | worked-out example | 2 - normal        |

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data types  
branch-1: basic if-statement  
excp-2, excp-3: raise exception, handle different exceptions

#### Learning Activities

1) read the given Python code
2) run the program in order to understand it  
3) write line comments to explain the code behaviour
4) explain your understanding to another student

#### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 5.6, Seiten 167-177

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

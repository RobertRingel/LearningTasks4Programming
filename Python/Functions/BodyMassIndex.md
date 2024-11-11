### Learning Task: Body-mass-index

Read the given Python code and complete the function implementation for the calculation of the body-mass-index.
Test the implementation by running the final program.

``` python
# --- calculation of the body-mass-index ---

def                                          # implement function header
    '''
    Calculates the body-mass-index as weight/height**2
        Args:
            weight(float): the body weight [kg]
            height(float): the body height [m]
        Returns:
            float: the body-mass-index
    '''
                                         	# implement calculation
                                         	# pass the result
	
w = float(input('Your weight [kg]:'))
h = float(input('Your height [m]:'))

bmi = calc_body_mass_index(w, h)
print('Your bmi:',bmi)
```

---------------------------------------
---------------------------------------

##### Solution

``` python
# --- calculation of the body-mass-index ---

def calc_body_mass_index(weight, height):
    '''
    Calculates the body-mass-index as weight/height**2
        Args:
            weight(float): the body weight [kg]
            height(float): the body height [m]
        Returns:
	    float: the body-mass-index
    '''
    bmi = weight/height**2
    return bmi

w = float(input('Your weight [kg]:'))
h = float(input('Your height [m]:'))

bmi = calc_body_mass_index(w, h)
print('Your bmi:',bmi)
```

##### Previous Knowledge

- basics of input-processing-output
- basic data types
  
##### Learning Activities

1) read the given Python code and the function documentation
2) complete the function implementation
3) run the program in order to test it

##### Supporting information

[tutorialspoint.com: function](https://www.tutorialspoint.com/python/python_functions.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 8, pages 129-155  

[www.python-kurs.eu: Funktionen](https://www.python-kurs.eu/python3_funktionen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 3, Seiten 71-82 und Kapitel 5, Seiten 177-200

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Functions 

*Learning objective:*  
- write a function implementation

[//]: # "learning objective: 1-function"
[//]: # "previous knowledge: 2-ipo"

*Complexity:*  1-low 

*Task type:*  completion task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

Topic: data structures - list

## Learning Task: Series of water level measurements

The following program can be used to process water level measurements using a list data structure.

Read the program, run it and write comments to the code.  

Finally answer the following question:  
Why is an infinite loop benefitial for this implementation?

``` python
# --- process water level measurements ---

water_level = []                            
while True:                                 
	val = int(input('Water level [cm]:'))
	if val >= 0:                            
		water_level.append(val)             
	else:
		break                               

avg = sum(water_level)/len(water_level)     
sum2 = 0.0
for v in water_level:
	sum2 = sum2 + (v-avg)**2
std_dev = (sum2/len(water_level))**0.5      

print('All measured water level values in centimeters:')
print(water_level)
print('min. value:',min(water_level))
print('max. value:',max(water_level))
print('avg. value:',avg)
print('std. deviation:',std_dev)
```

---------------------------------------

### Solution

``` python
# --- process water level measurements ---

water_level = []                            # the list variable to store the values
while True:                                 # loop to enter data
	val = int(input('Water level [cm]:'))
	if val >= 0:                            # level >= 0 cm?
		water_level.append(val)             # yes: store the value at end of list
	else:
		break                               # no: ... invalid value, break loop

avg = sum(water_level)/len(water_level)     # calculate average water level
sum2 = 0.0
for v in water_level:
	sum2 = sum2 + (v-avg)**2
std_dev = (sum2/len(water_level))**0.5      # calculate standard deviation

# show data and basic statistics
print('All measured water level values in centimeters:')
print(water_level)
print('min. value:',min(water_level))
print('max. value:',max(water_level))
print('avg. value:',avg)
print('std. deviation:',std_dev)
```

Answer to the question: Why is an infinite loop benefitial for this implementation?  
Because an infinite loop allows the user to enter non-predefined number of measured values.  

#### Previous Knowledge

vcp-1: print, variable, calculations  
branch-2: if-break  
loop-2: while-loop incl. break  
list-1: list, for-iteration, basic list-functions  
  
#### Learning Activities

1) read the Python code
2) get an understanding of the code
3) write comments to the code
4) thinking about coding decision

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
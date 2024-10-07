### Learning Task: Water level moving average

The following program stores water levels and calculates the moving average of the last three values stored in the list.

Read the program, run the program and add comments to the code to document your understanding.

``` python
print('--- Water levels: calculation of the moving average ---')
values = []                                    

while True:                                    
	v = float(input('new water level [cm]:'))  
	if v<0.0:                                  
		break                                  
	values.append(v)                           
	n = len(values)                            
	if n >= 3:                                 
		mv_avg = sum(values[n-3:])/3           
		print('moving average:',mv_avg)        

print('End.')
```

---------------------------------------
---------------------------------------

##### Solution

``` python
print('--- Water levels: calculation of the moving average ---')
values = []                                    # list of values

while True:                                    # loop to enter and process values
	v = float(input('new water level [cm]:'))  # enter water level value
	if v<0.0:                                  # negative water level?
		break                                  # yes: terminate loop
	values.append(v)                           # add value to list
	n = len(values)                            # n: current number of values
	if n >= 3:                                 # n>3?
		mv_avg = sum(values[n-3:])/3           # yes: calculate moving average
		print('moving average:',mv_avg)        #      print mvg. average

print('End.')
```


##### Previous Knowledge

- basic list operations
- list item access by index
- loops and branches
  
##### Learning Activities

1) read the Python code
2) run and test the program
3) get an understanding of the code
4) get an understanding of the moving average
5) write comments to the new code
6) draw a sketch of the new data structure


###### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)
Theis, T. G. P. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 109-116

----
[//]: # "Learning objective: Basic list operations"
[//]: # "Topic: List data structures"
[//]: # "Complexity: 2 - normal"
[//]: # "Task type: worked-out example"

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2024            
License: CC BY-SA 4.0

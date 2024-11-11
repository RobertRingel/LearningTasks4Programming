### Learning Task: Update exchange rates

The following Python program ist used to show and update currency exchange rates. Read the code and run the code to obtain an understanding.
Focus on the function "update_rates" in order to write the function documentation based on Google-Doc-Style.
How will the updated exchange rates be usable in the main part of the program without a function return statement?

Explain your understanding to another student.

``` python
exchange_rates = {'GBP-USD':1.30, 'EUR-USD':1.09, 'USD-EUR':0.91, 'GBP-EUR':1.19, 'YEN-USD':0.0066}

def print_rates_table(rates):
	"""
	Prints currency exchange rates in a simple table format.

	Args:
		rates (dict): the rates as currencies : rate
	"""
	keys = sorted(rates.keys())
	for k in keys:
		print(k,':',rates[k])

def update_rates(rates):
	curr1 = input('From currency:')
	curr2 = input('To currency  :')
	key = curr1+'-'+curr2
	rate = float(input('Rate         :'))
	if rate < 0.0:
		print('Invalid rate!')
		return
	rates[key] = rate

	
print_rates_table(exchange_rates)
update_rates(exchange_rates)
print_rates_table(exchange_rates)
```

---------------------------------------
---------------------------------------

##### Solution

``` python
exchange_rates = {'GBP-USD':1.30, 'EUR-USD':1.09, 'USD-EUR':0.91, 'GBP-EUR':1.19, 'YEN-USD':0.0066}

def print_rates_table(rates):
	"""
	Prints currency exchange rates in a simple table format.

	Args:
		rates (dict): the rates as currencies : rate
	"""
	keys = sorted(rates.keys())    # get a sorted list of currencies
	for k in keys:
		print(k,':',rates[k])      # print currency and exchange rate

def update_rates(rates):
	"""
	Updates currency exchange rates according to user input.
	Invalid rates will not be accepted by the update.

	Args:
		rates (dict): the rates as currencies : rate
	"""
	curr1 = input('From currency:')
	curr2 = input('To currency  :')
	key = curr1+'-'+curr2                   # create a combined dictionary key
	rate = float(input('Rate         :'))
	if rate < 0.0:                          # invalid rate?
		print('Invalid rate!')              # yes: print message
		return                              #      end function
	rates[key] = rate                       # update exchange rate
	
	

print_rates_table(exchange_rates)           # show current exchange rates
update_rates(exchange_rates)                # update exchange data
print_rates_table(exchange_rates)           # show new exchange data
```
**Answer to this question:**  
How will the updated exchange rates be usable in the main part of the program without a function return statement?  

The function argument 'rates' is a dictionary. A dictionary, as any other data structure, will be passed as reference to the function. 
Therefore any change inside the data structure will be made in the original data structure. So it is automatically visible at any position in the source code.


##### Previous Knowledge

- basics of input-processing-output
- basics of branches
- basics of dictionaries
  
##### Learning Activities

1) run and read the given Python code 
2) write the function documentation
3) get an answer to the given question
4) explain the understanding and the answer to the question to another student

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
- understand data structures as function arguments

[//]: # "learning objective: 1-function"
[//]: # "previous knowledge: 2-ipo 2-dict 1-branch"

*Complexity:*  1-low 

*Task type:*  worked-out example 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024            
License: CC BY-SA 4.0

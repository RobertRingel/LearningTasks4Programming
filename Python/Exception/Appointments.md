### Learning Task: Appointments

The following Python program is used to store user input for appointments. The 
entered data is checked for validity before it will be stored. In case of 
invalid data an error will be raised and shown.

Read the code and run it to obtain an understanding. Then write a similar
Python program for anonther use case - e.g. get and store birthday data.

``` python
# --- program to store appointment data ---

def get_appointment():
	name = input('Name or Pupose:')
	if name == '':                                     # valid name?
		raise ValueError('Missing name information.')  # no: raise error

	date = input('Date dd.mm.yyyy:')
	tokens = date.split('.')
	if len(tokens) != 3:                               # vaild date?
		raise ValueError('Invalid date:'+date)         # no: raise error

	time = input('Time hh:mm:')
	tokens = time.split(':')
	if len(tokens) != 2:                               # vaild time?
		raise ValueError('Invalid date:'+time)         # no: raise error

	loc = input('Location:')
	if loc == '':                                      # valid location?
		raise ValueError('Missing location.')          # no: raise error

	record = (name, date, time, loc)                   # create record
	return record                                      # return record

appointments = []
while len(appointments) < 3:             # get 3 Appointments
	try:                                 # try
		info = get_appointment()         #   ... risky function call
	except Exception as e:               # catch potential exceptions
		print('There was an error!')
		print(e)
	else:
		appointments.append(info)        # store valid data

print(appointments)
```
**Note:** The shown Python program performs only a very brief check for validity
of the entered data. More elaborated checks should include the validity of the 
numeric time and date data. A professional approach would use regular expressions.


---------------------------------------
---------------------------------------

#### Solution

``` python
# --- program to store birthday data ---

def get_birthday():
	name = input('Name:')
	if name == '':                                     # valid name?
		raise ValueError('Missing name information.')  # no: raise error

	date = input('Birthday dd.mm.yyyy:')
	tokens = date.split('.')
	if len(tokens) != 3:                               # vaild date?
		raise ValueError('Invalid date:'+date)         # no: raise error

	record = (name, date)                              # create record
	return record                                      # return record

bdays = []
while len(bdays) < 3:                    # get 3 birthdays
	try:                                 # try
		info = get_birthday()            #   ... risky function call
	except Exception as e:               # catch potential exceptions
		print('There was an error!')
		print(e)
	else:
		bdays.append(info)               # store valid data

print(bdays)
```
... or any other similar Python program.

##### Previous Knowledge

- basics of loops and branches
- basics of lists
- basics of functions
  
##### Learning Activities

1) read and run the given Python code
2) write similar Python program to check the validity of user input
3) test and run the program

##### Supporting information

[tutorialspoint.com: Exception handling](https://www.tutorialspoint.com/python/python_tryexcept_block.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 10, pages 194-201  

[www.python-kurs.eu: Ausnahmebehandlung](https://www.python-kurs.eu/python3_ausnahmebehandlung.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 5.6, Seiten 167-177

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Exceptions 

*Learning objective:*  
- implement exception handling

[//]: # "learning objective: 1-exception"
[//]: # "previous knowledge: 1-loop 1-branch 1-list 2-function"

*Complexity:*  1-low

*Task type:*  imitation task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 01/2025  
License: CC BY-SA 4.0

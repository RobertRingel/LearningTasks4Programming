### Learning Task: Priority tasks

The given Python code implements three priority levels for three task lists. The user can see the tasks in the different priority levels.
He can add new tasks or remove listed tasks.   

In order to run this program it is required to design and implement the related dictionary data structure as follows:  
There are three priority classes: top, high, normal  
For each of this classes exists a list of tasks in the form of simple text messages, such as 'clean the kitchen'

Fill the dictionary with sample data, run and test the program!

``` python
# --- prio todo-list ----

tasks = {        # ...
                 # fill this dictionary with valid sample data
	             # ...
        }

while True:
	print('\n--------------------------')
	prio = input('Which priority (top/high/normal)? ')     # user enters priority 
	if prio == 'end':                                      # end -> terminate program
		break
	if prio in tasks.keys():	                           # check for valid priority
		todos = tasks.get(prio)                            # todos: list of tasks in requested prio
		i = 0
		print('--- Task List ---')                         # print tasks and related index
		for t in todos:
			print(i,':',t)
			i = i +1
		print('-1: add new task')
	
		index = int(input('Enter number to remove task or -1 to add a new one: '))
		if index == -1:                                    # user will enter a new task
			action = input('new task: ')                   
			todos.append(action)                           # append new task to task list
		else:
			if index>=0 and index<len(todos):              # check for valid index
				todos.pop(index)                           # remove task from task list
```

---------------------------------------
---------------------------------------

##### Solution

``` python
# --- prio todo-list ----

# dictionary of task lists related to 3 prority classes
tasks = {'top' : ['buy X-mas presents'], 
	     'high' : ['clean kitchen','clean bath room'],
   		 'normal' : ['prepare 4 exam'] }

while True:
	print('\n--------------------------')
	prio = input('Which priority (top/high/normal)? ')     # user enters priority 
	if prio == 'end':                                      # end -> terminate program
		break
	if prio in tasks.keys():	                           # check for valid priority
		todos = tasks.get(prio)                            # todos: list of tasks in requested prio
		i = 0
		print('--- Task List ---')                         # print tasks and related index
		for t in todos:
			print(i,':',t)
			i = i +1
		print('-1: add new task')
	
		index = int(input('Enter number to remove task or -1 to add a new one: '))
		if index == -1:                                    # user will enter a new task
			action = input('new task: ')                   
			todos.append(action)                           # append new task to task list
		else:
			if index>=0 and index<len(todos):              # check for valid index
				todos.pop(index)                           # remove task from task list
```

##### Previous Knowledge

- loops, branches, lists
- dictionary to store lists
  
##### Learning Activities

1) read and understand the given code
2) write sample data into the dictionary definition
3) run and test the program

##### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 120-125 

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Dictionary data structures 

*Learning objective:*  
- definition of dictionary to store lists

[//]: # "learning objective: 3-dictionary"
[//]: # "previous knowledge: 3-dictionary 2-list 1-loop 2-branch"

*Complexity:*  2-normal 

*Task type:*  completion task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0
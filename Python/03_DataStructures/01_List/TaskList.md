Topic: data structures - list

## Learning Task: Basic task list

Write a Python program that can be used as a task list. The user has the choice to add a new task to the list or the user can remove the top task from the list. After that the program shall show the current task list. A task is just a string, containing a note of something to be done. All the tasks shall be stored in a list.

Implement the program, test it, write comments to the code and explain the program to another student when finished.

---------------------------------------

### Solution

``` python
print('--- My personal task list ---')

todo = []                               # the task list

act = ''                                # user activity
while act != '0':                       # loop as long as user will do something
	print()                             # print a mini menue
	print('1: add task  2: remove top task  0: end program')
	act = input('your choice: ')        # user enters activity
	
	if act == '1':                      # add task?
		task = input('New task : ')     # yes: enter task text
		todo.append(task)               #      store task at end of list
		print(todo)                     #      print current task list
	elif act == '2':                    # remove top task?
		todo.pop(0)                     # yes: remove top task
		print(todo)                     #      print current task list
print('program ended')
```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| basic list data structure operations           | conventional task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-2: if-elif  
loop-1: while-loop  
list-1, list-2: list, list operations  

#### Learning Activities

1) understand the task
2) implement Python code 
3) run the Python code and check the result
4) add comments to the code
5) explain the program to somebody else

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

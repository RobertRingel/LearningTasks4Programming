Topic: data structures - list

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
todo = ['1: water my plants','5: buy movies tickets']

select = ''
while select != '0':
	print()
	print('1: add task  2: remove top task  0: end program')
	select = input('your choice: ')
	
	if select == '1':
		task = input('New task (Prio: Note): ')
		todo.append(task)
		todo.sort()
		print(todo)
	elif select == '2':
		todo.pop(0)
		print(todo)
print('program ended')
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used as a task list for prioritized tasks. It can add and remove tasks including a task related priority.

*Programming task*  
Write a Python program to implement a prioritized task list. The user shall be able to add a task to the list or to remove a task from top of the list. After such an action, the program shall print the priority-ranked list of tasks. A task is just a string representing a ToDo-note, where the first character is a digit that stands for the task's priority.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| basic list data structure operations           | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input  
loop-1: while-loop  
list-2: list operations like sort and pop  

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: lists](https://www.tutorialspoint.com/python/python_lists.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 3, pages 33-48  

[www.python-kurs.eu: Listen](https://www.python-kurs.eu/python3_listen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 109-116

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

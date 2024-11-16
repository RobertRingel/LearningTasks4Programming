### Learning Task: ToDo list

The following Python program can be used to manage your task list. All tasks
are stored in the text file 'ToDoList.txt'.

First open the text file to understand its content. Then read the code and run
it to obtain an understanding. 
Finally add the missing lines at the end of the programm to write the task list
data in the text file. This is required to save any changes in the task list
back to the text file.
Check the content of the text file after it has been written by the program.

``` python
todo = []                           # task list 

# ----- read file -----
file_name = 'ToDoList.txt'         
todo_file = open(file_name, 'r')    # open file for reading

while True:                         # loop to read from file
    line = todo_file.readline()     # read one line
    line = line.strip('\n')         # remove line break from line string
    if line == '':                  # no data -> break loop
        break
    todo.append(line)               # append line to task list

todo_file.close()                   # close text file

# ----- core program -----
select = ''
while select != '0':
    print()
    print('1: add task  2: remove top task  0: end program')
    select = input('your choice: ')
    
    if select == '1':               # user will enter new task  
        task = input('New task (Prio: Note): ')
        todo.append(task)           # append task to task list
        todo.sort()                 # sort task list
        print(todo)                 # show task list
    elif select == '2':             # user will remove top task
        todo.pop(0)                 # remove top task
        print(todo)                 # show task list

# ----- write file ------




print('program ended')
```

---------------------------------------
---------------------------------------

#### Solution

``` python
todo = []                           # task list 

# ----- read file -----
file_name = 'ToDoList.txt'         
todo_file = open(file_name, 'r')    # open file for reading

while True:                         # loop to read from file
    line = todo_file.readline()     # read one line
    line = line.strip('\n')         # remove line break from line string
    if line == '':                  # no data -> break loop
        break
    todo.append(line)               # append line to task list

todo_file.close()                   # close text file

# ----- core program -----
select = ''
while select != '0':
    print()
    print('1: add task  2: remove top task  0: end program')
    select = input('your choice: ')
    
    if select == '1':               # user will enter new task  
        task = input('New task (Prio: Note): ')
        todo.append(task)           # append task to task list
        todo.sort()                 # sort task list
        print(todo)                 # show task list
    elif select == '2':             # user will remove top task
        todo.pop(0)                 # remove top task
        print(todo)                 # show task list

# ----- write file ------
todo_file = open(file_name, 'w')    # open file for writing
for task in todo:                   # iterate all tasks
    todo_file.write(task+'\n')      # write task to file
todo_file.close()                   # close file

print('program ended')
```

##### Previous Knowledge

- basics of input-processing-output
- basics of loops and branches
- basics of lists
  
##### Learning Activities

1) understand content of the text file
2) read and run the given Python code
3) implement the required Python commands to store the task list as text file
4) check the content of the text file after it has been written

##### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  
Kapitel 8, Seiten 257-270

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Text files

*Learning objective:*  
- understand reading and writing text files

[//]: # "learning objective: 2-files"
[//]: # "previous knowledge: 1-list 1-branch 1-loop"

*Complexity:*  2-normal

*Task type:*  completion task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
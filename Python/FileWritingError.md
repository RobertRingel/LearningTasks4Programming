### Learning Task: File-Writing Error

The given Python code will write user input data for student names and exam scores to a text file on a USB stick.
Start the program with an USB stick attached to your computer. Remove the USB stick after you have entered some data while the program is still running. Add some more data and then enter 'END' to terminate the program regulary. The program will crash, because the storage location is not available any longer. Explore this behaviour.  
Add the appropriate exception handling to prevent the program crash in such situations. Print a warning to the user that states that the data was not able to be stored. Finally run the program again to proof the functionality of your implementation.  

``` python
file_name = '/media/robert/3BD1/exam_marks.txt'  # file name for a Linux USB file
DELIMITER = ','

grades_file = open(file_name, 'w')    

while True:
	name = input('Name:')
	if name == 'END':
		break
	score = input('Score:')
	line = name + DELIMITER + score + '\n'
	grades_file.write(line)

grades_file.close()                    

```

---------------------------------------
---------------------------------------

##### Solution

``` python
file_name = '/media/robert/3BD1-CAA4/exam_marks.txt'              # the file name
DELIMITER = ','

try:

	grades_file = open(file_name, 'w')     
	while True:
		name = input('Name:')
		if name == 'END':
			break
		score = input('Score:')
		line = name + DELIMITER + score + '\n'
		grades_file.write(line)

	grades_file.close()                   

except IOError as err:
	print('Error by file operation:',err)
	print('The data was not stored!')
```

##### Previous Knowledge

- basics of writing text files
- basic loops and branches
  
##### Learning Activities

1) read the given Python code 
2) run the program in order to test it for the specific situation 
3) implement the requested exception handling 
4) test the exception handling

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
- implement basic exception handling

[//]: # "learning objective: 1-exception"
[//]: # "previous knowledge: 2-ipo 2-loop 1-branch 1-files"

*Complexity:*  2-normal 

*Task type:*  completion task

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 01/2025            
License: CC BY-SA 4.0

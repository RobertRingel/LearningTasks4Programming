Topic:  data structures - dictionary

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

Finally feel free to write comments to the code.

``` python
stud_grade = {'Max':['Math', 2.0, 'Phys', 2.7, 'Chem',1.3], 
              'Liz':['Math', 1.3, 'Phys', 2.0, 'Chem',1.0], 
              'Joe':['Math', 3.0, 'Phys', 2.7, 'Chem',3.3] }

print('--- average student grading ---')
for s in stud_grade.keys():
	gradings = stud_grade.get(s)
	marks = gradings[1::2]
	avg = sum(marks)/len(marks)
	print(s,"%.2f " % avg)
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program is used to calculate the average student grading based on the list of exam marks for each student.

*Programming task*  
Write a Python program to calculate the average student grading based on the list of exam marks for each student. Use a dictionary data structure to store the lecture names and the exam marks as a list related to every student's name.
Use the following print statement to print just two decimals for the calculated average grading: print("%.2f " % avg)

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| iterate a dictionary based on the keys-view    | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-3: variable, calculations, formatted printing  
list-1, list-3: basic list, for-iteration, list slicing  
dict-2, dict-3: get all dictionary keys, dictionary stores lists  

#### Learning Activities

1) reading and running Python code
2) explain the purpose in a short and specific written statement
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 120-125

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
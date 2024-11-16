### Learning Task: My event

Write a Python program that helps you to organize a party event.  
All important data as well as a list of guests shall be stored in the text file
'MyEvent.txt'. After program start the program will read this file in order to
print all the current data out of the file. Then the user will have a chance to
enter more data to be added to the text file.

A sample text file 'MyEvent.txt' is provided here in the task pool.

Write the related Python program including line comments. Test the program and
demonstrate and explain it to another student.

---------------------------------------
---------------------------------------

##### Solution

``` python
file_name = 'MyEvent.txt'                     # the file name
event_file = open(file_name, 'r')             # open the text file for reading 

while True:                                   # loop to read line by line
    line = event_file.readline()              # read one line of text
    line = line.strip()                       # remove line break 
    if line == '':                            # empty line -> stop reading
        break
    print(line)                               

event_file.close()                            # close text file

print()
add_data = input('Enter more guests (y/n)?')
if add_data == 'y':
    event_file = open(file_name, 'a')         # open the text file to append data 
    while True:                               # loop to enter guests
        info = input('Guest information: ')   # enter guest info
        if info == '':                        # no info -> break loop
            break
        event_file.write(info+'\n')           # append guest info to file

    event_file.close()                        # close file
```

##### Previous Knowledge

- basics of input-processing-output
- basics of loops and brances
  
##### Learning Activities

1) read and understand the given task
2) understand the file format
3) implement the Python code
3) test the written code
4) add comments to the code
5) explain the code to another student

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
- read and write to append to text files

[//]: # "learning objective: 3-files"
[//]: # "previous knowledge: 1-ipo 1-loop 1-branch 1-files"

*Complexity:*  2-normal

*Task type:*  conventional task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
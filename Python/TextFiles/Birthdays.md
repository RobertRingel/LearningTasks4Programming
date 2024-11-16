### Learning Task: Birthdays

The following Python program reads birthday data from a text file. The user
enters a particular date and the program prints the birthday data for this
specific date as it was read from the file.

Read the code and run it to obtain an understanding. Then write a similar
Python program for anonther use case - e.g. look-up a person's name to show the
phone number or email address.

``` python
file_name = 'Birthdays.txt'              # the file name
birthday_file = open(file_name, 'r')     # open file for reading

search_date = input('Requested date:')   # ask user for date

while True:                              # read file line by line
    line = birthday_file.readline()      # read one line from the file
    line = line.strip('\n')              # remove line break from line data
    if line == '':                       # empty line -> terminate reading
        break
    data = line.split('\t')              # split line data by '\t'
    if data[1] == search_date:           # check for requested date
        print(line)                      # print line

birthday_file.close()                    # close text file
```

---------------------------------------
---------------------------------------

#### Solution

``` python
file_name = 'Contacts.txt'               # the file name
contact_file = open(file_name, 'r')      # open file for reading

search_name = input('Requested name:')   # ask user for name

while True:                              # read file line by line
    line = contact_file.readline()       # read one line from the file
    line = line.strip('\n')              # remove line break from line data
    if line == '':                       # empty line -> terminate reading
        break
    data = line.split('\t')              # split line data by '\t'
    if data[0] == search_name:           # check for requested name
        print(line)                      # print line

contact_file.close()                     # close text file
```
... or any other similar Python program.

##### Previous Knowledge

- basics of loops and branches
- basics of lists
  
##### Learning Activities

1) read and run the given Python code
2) write similar Python program to read data from file
3) test and run the program

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
- reading text files

[//]: # "learning objective: 1-files"
[//]: # "previous knowledge: 1-branch 1-loop 1-list"

*Complexity:*  1-low

*Task type:*  imitation task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
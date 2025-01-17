### Learning Task: Wrong file name

The given Python code will read the content of the text file 'ExchangeRates.txt'. Unfortunately there is a typo in the file name causing the program to crash.  
Add the appropriate exception handling to prevent the program crash when a named file is not available. In such a situation print a warning to the user.  
Improve the given code in a way, that reading and closing the file will only be performed, if the file was opened successfully.
Finally run the program to proof the functionality of your implementation.  

``` python
file_name = 'ExchangeRateS.txt'      # the file name
rates_file = open(file_name, 'r')    # open file for reading
while True:                          # read file line by line
    line = rates_file.readline()     # read one line from the file
    if line == '':                   # empty line -> terminate reading
        break
    print(line)                      # print line

rates_file.close()                   # close text file                   
```

---------------------------------------
---------------------------------------

##### Solution

``` python
file_name = 'ExchangeRateS.txt'              # the file name
error = False                                # error state variable
try:
	rates_file = open(file_name, 'r')        # open file for reading
except Exception as e:
	print('Error opening file:'+file_name)   # print error message
	print(e)
	error = True                             # set the error state

while not error:                             # no error: read file line by line
    line = rates_file.readline()             #   read one line from the file
    if line == '':                           #   empty line -> terminate reading
        break
    print(line)                              #   print line

if not error:                                # no error:
	rates_file.close()                       #    close text file
```

##### Previous Knowledge

- basics of reading text files
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
- implement exception handling

[//]: # "learning objective: 1-exception"
[//]: # "previous knowledge: 2-loop 1-branch 1-files"

*Complexity:*  2-normal 

*Task type:*  completion task

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 01/2025            
License: CC BY-SA 4.0

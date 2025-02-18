Topic: text files

## Learning Task: Exchange rates

The following Python program can be used to calculate currency exchanges. The
related exchange rates are stored in the text file 'ExchangeRates.txt'.

First open the text file to understand its content. Then read the code and run
it to obtain an understanding. After that, write comments to the lines required 
to read the text file into the list data structure of the program.  
Finally explain your understanding to another student.

If you like, feel free to add some more currency exchange rates to the text file
and check, that they will be read correctly by the Python program.

``` python
currencies = []                    # data of currencies and rates

file_name = 'ExchangeRates.txt'    # name of the text file
rate_file = open(file_name, 'r')

while True:
    line = rate_file.readline()
    if line == '':
        break
    data = line.split(';')
    src = data[0]
    dest = data[1]
    rate = float(data[2])
    currencies.append(src)
    currencies.append(dest)
    currencies.append(rate)

rate_file.close()

# --- core functionalty of the program ---
src = input('From what currency:')
dest = input('To what currency:')

i=0                                         # list index
# loop to loock up the required rate and to perform the calculation
while i<len(currencies):
    if src == currencies[i] and dest == currencies[i+1]:  # currencies found?
        rate = currencies[i+2]                            # yes: get rate
        amount = float(input('Amount:'))                  #      ask for amount
        exchange = amount*rate                            #      calc. exchange
        print('You will get:',exchange,dest)              #      print result
        break                                             #      break loop
    i=i+3                                                 # no:  increment index

if i>=len(currencies):                      # currencies not found
    print('This is not possible.')          #     print message
```

---------------------------------------

### Solution

``` python
# data of currencies and rates - structure: soure - dest - rate
currencies = []                  

file_name = 'ExchangeRates.txt'    # name of the text file 
rate_file = open(file_name, 'r')   # open text file for reading

while True:
    line = rate_file.readline()    # read a line from the file
    if line == '':
        break                      # break loop in case of empty line
    data = line.split(';')         # split line content by ;
    src = data[0]                  # get source currency
    dest = data[1]                 # get destination currency
    rate = float(data[2])          # get exchange rate as float
    # store all data elements in the list
    currencies.append(src)         
    currencies.append(dest)
    currencies.append(rate)

rate_file.close()                  # close the text file

# --- core functionalty of the program ---
src = input('From what currency:')
dest = input('To what currency:')

i=0     # list index
# loop to loock up the required rate and to perform the calculation
while i<len(currencies):
    if src == currencies[i] and dest == currencies[i+1]:    # currencies found?
        rate = currencies[i+2]                              # yes: get rate
        amount = float(input('Amount:'))                    #      ask for amount
        exchange = amount*rate                              #      calc. exchange
        print('You will get:',exchange,dest)                #      print result
        break                                               #      break loop
    i=i+3                                                   # no:  increment index

if i>=len(currencies):                      # currencies not found
    print('This is not possible.')          #     print message

```

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| understand reading text files into a data structure | worked-out example | 3 - high       |

#### Previous Knowledge

vcp-1, vcp-2: print, variable, calculations, input, type conversion  
string-2: important string operations  
branch-1: basic if  
loop-1, loop-2: basic while loop, while-break loop  
list-1: basic list operations and list index access  
file-1: basic file reading  

#### Learning Activities

1) understand content of the text file
2) run and read the given Python code
3) write commentes the file related lines
4) explain the understanding to another student
5) change content of the text file and run the program to check it is read correctly

#### Supporting information

[geeksforgeeks.org: text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 10, pages 183-198  

[www.python-kurs.eu: Dateien](https://www.python-kurs.eu/python3_dateien.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:  
Kapitel 8, Seiten 257-270

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
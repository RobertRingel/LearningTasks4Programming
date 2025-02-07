Topic: Tuple data structures

## Learning Task: Check lottery guess

Complete the given lines of Python code to check a lottery guess. 
Because a lottery guess should never be changed the variables a -f shall be stored as a tuple in the variable guess.
For this guess every number needs to be checked to be greater zero and less then 50 for the '1 out of 49 lottery'. 
Furthermore it does not make sence that any number is guessed more then once in such a guess. This needs also be checked.
The result of the checking procedure will be printed to the user.

Complete the program, run it and test it and do not forget to add comments to the code.  
Compare your coding result with another student.

*Hint:*  
The count-operation of a tuple can be used to check how often a certain value is contained in a tuple:  
c = guess.count(5)  ... will count how often the value 5 is stored in the tuple-variable guess

``` python
# --- check lottery guess ---

a = int(input('Number 1:'))
b = int(input('Number 2:'))
c = int(input('Number 3:'))
d = int(input('Number 4:'))
e = int(input('Number 5:'))
f = int(input('Number 6:'))

result = 'valid'
guess =  

for number in ...

    ...



print('This guess is',result)
```

---------------------------------------

### Solution

``` python
# --- check lottery guess ---

a = int(input('Number 1:'))
b = int(input('Number 2:'))
c = int(input('Number 3:'))
d = int(input('Number 4:'))
e = int(input('Number 5:'))
f = int(input('Number 6:'))

result = 'valid'                                      # the check result
guess = (a,b,c,d,e,f)                                 # define guess as a tuple

for number in guess:                                  # iterate all the numbers to check them
	if number<1 or number>49:                         # number is valid?
		print('invalid number:',number)               # no:  print message
		result = 'invalid'                            #      invalid result
	if guess.count(number)>1:                         # number is guessed more than once?
		print('multiple entries for number:',number)  # yes: print message
		result = 'invalid'                            #      invalid guess

print('This guess is',result)
```

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| definition and iteration of a tuple            | completion task | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable, data type  
branch-1: simple if  
tuple-1: define a tuple, for-iteration
  
#### Learning Activities

1) read and understand the task
2) read and understand the given code
3) define a tuple variable
4) implement code to iterate and check the tuple
5) test the written code
6) add comments to the code
7) compare the code with another student

#### Supporting information

[tutorialspoint.com: tuple](https://www.tutorialspoint.com/python/python_tuples.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 4, pages 65-67  

[www.python-kurs.eu: Tupel](https://www.python-kurs.eu/python3_sequentielle_datentypen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 4, Seiten 116-132

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0
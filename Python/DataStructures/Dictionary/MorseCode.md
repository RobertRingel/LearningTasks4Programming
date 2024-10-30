### Learning Task: Morse code translator

Given is the dictionary code that provides the related Morse code for every letter. 
The given Python code below illustrates how the letters of a string can be printed separately.

Complete the program in way, that it will print the related Morse code for the text stored in the variable message.

Complete the program, run it and test it and do not forget to add comments to the code.  
Compare your coding result with another student.

``` python
# --- Morse Code Translator ---

code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 
        'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
        'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
        'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
        'Y':'-.--', 'Z':'--..', ' ':' '}

message = "Hello World"
print("String is:", message)
print("Characters of string:")
for char in message.upper():
	print(char, end=' ')
```
---------------------------------------
---------------------------------------

##### Solution

``` python
# --- Morse Code Translator ---

# the Morse code stored in a dictionary
code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 
        'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
        'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
        'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
        'Y':'-.--', 'Z':'--..', ' ':'   '}

message = "Hello World"           # the message to be coded
print("String is:", message)
print("Morse code of string:")
for char in message.upper():      # convert message to upper case and iterate all characters
	morse_code = code[char]       # get Morse code for one character
	print(morse_code, end=' ')    # print the Morse code
print()
```

##### Previous Knowledge

- basics of dictionaries
- basics of strings
  
##### Learning Activities

1) read and understand the given code
2) implement commands to access the dictionary content
3) test the written code
4) add comments to the code
5) compare the code with another student

##### Supporting information

[tutorialspoint.com: dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 6, pages 92-105  

[www.python-kurs.eu: Dictionary](https://www.python-kurs.eu/python3_dictionaries.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.:   
Kapitel 4, Seiten 120-125

---------------------------------------
---------------------------------------
#### Meta-Information
*Topic:*  Dictionary data structures 

*Learning objective:*  
- access data of a dictionary

[//]: # "learning objective: 1-dictionary"
[//]: # "previous knowledge: 1-dictionary 2-string"

*Complexity:*  1-low 

*Task type:*  completion task 

----
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2024            
License: CC BY-SA 4.0

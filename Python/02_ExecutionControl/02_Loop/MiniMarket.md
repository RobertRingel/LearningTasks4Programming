Topic: controlling program execution - loop

## Learning Task: What is the purpose of the code?

Read, analyse and run the given Python program. What is it's purpose?  
Write the text for a related programming task.

``` python
# ---- initialize variables -------
sum_price = 0.0      # total price
sum_vat = 0.0        # total VAT

# ---- loop to enter user data and cumulate values -----
while True:
    name = input("Product: ")                 # enter product name as string
    if name == "":                            # check for product name
        break                                 # break loop if no product name is given
    
    price = float(input("Price  : "))         # enter price as float
    pcs = int(input("Pieces : "))             # enter pieces as integer
    vat = float(input("VAT %  : "))           # enter VAT as float
    
    sum_price = sum_price + price*pcs         # cumulate prices
    sum_vat = sum_vat + price*pcs*vat/100.0   # cumulate VAT
    
    # print cumulated values
    print(sum_price, "EUR plus ", sum_vat, "EUR VAT \n")

print("The end :-)")
```

---------------------------------------

### Solution

*Purpose of the program:*  
The program can be used as a mini market cash point calculator.

*Programming task*  
Write a Python program to be used as a mini market cash point calculator.  
The user will enter product name, price, number of pieces and VAT for a series of products and the program will calculate the total price and the total VAT.

---------------------------------------

| **Learning objective**                         | **Task type**   | **Complexity** |
| ---------------------------------------------- | --------------- | -------------- |
| loop to repeat code sections, break a loop     | reverse task    | 2 - normal     |  

#### Previous Knowledge

vcp-1, vcp-2: print, input, variable  
branch-1: if-statement  
loop-2: while-loop including break-statement  
  
#### Learning Activities

1) read, run and understand the Python code
2) explain the purpose in a short and specific written statement.
3) write a short and specific programming task, that yields the given Python code

#### Supporting information

[tutorialspoint.com: while-loops](https://www.tutorialspoint.com/python/python_while_loops.htm)  
[tutorialspoint.com: break-Statement](https://www.tutorialspoint.com/python/python_break_statement.htm)  
Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.: Chapter 7, pages 118-121

[www.python-kurs.eu: Schleifen](https://python-kurs.eu/python3_schleifen.php)  
Theis, T. (2017). Einstieg in Python. In Rheinwerk Computing (5., aktualisierte Auflage). Rheinwerk Verlag GmbH.: Kapitel 3, Seiten 60-62

---------------------------------------

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 02/2025  
License: CC BY-SA 4.0

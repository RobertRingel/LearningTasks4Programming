### Learning Task: Slide show

The following Python program shall perform an image slide show. All data to
perform the show is stored in the text file 'SlideShow.cfg'.

Open the text file 'SlideShow.cfg' to get an understanding of the provided
data. Then read the given Python code.  

Complete the code by writing the missing commands for reading the data out of
the text file. Test the final program and enjoy the slide show.  
May you like to design a slide show of your own? Feel free to write your own 
slide show in a text file and to perform it by this Python program.

``` python
import matplotlib.pyplot as plt             # import module to show an image as plot
import matplotlib.image as mpimg            # import module to read an image file

file_name = 'SlideShow.cfg'                 # file name of the slide show definition
...                                         # open the text file

while True:                                 # loop
    img_file_name = ...                     # read image file name
    img_file_name = ...                     # remove line break 
    ...                                     # no file name -> stop the slide show
        break
    message = ...                           # read message from file
    message = ...                           # remove line break
    license = ...                           # read image license from file
    license = ...                           # remove line break
    delay = ...                             # read delay value from file
    delay = ...                             # convert delay to integer

    img = mpimg.imread(img_file_name)       # read the real image file

    plt.rcParams['toolbar'] = 'None'        # prepare image show
    plt.axis('off')                         # prepare image show
    note = message+"\n"+license             # init. the image note
    plt.title(note, fontsize=10)            # plot the image title
    plt.imshow(img)                         # plot the image
    plt.show(block=False)                   # show it
    plt.pause(delay)                        # pause for delay duration
    plt.close()                             # close the image plot

cfg_file.close()                            # close the text file
```

---------------------------------------
---------------------------------------

#### Solution

``` python
import matplotlib.pyplot as plt             # import module to show an image as plot
import matplotlib.image as mpimg            # import module to read an image file

file_name = 'SlideShow.cfg'                 # file name of the slide show definition
cfg_file = open(file_name, 'r')             # open the text file

while True:                                 # loop
    img_file_name = cfg_file.readline()     # read image file name
    img_file_name = img_file_name.strip()   # remove line break 
    if img_file_name == '':                 # no file name -> stop the slide show
        break
    message = cfg_file.readline()           # read message from file
    message = message.strip()               # remove line break
    license = cfg_file.readline()           # read image license from file
    license = license.strip()               # remove line break
    delay = cfg_file.readline()             # read delay value from file
    delay = int(delay.strip())              # convert delay to integer

    img = mpimg.imread(img_file_name)       # read the real image file

    plt.rcParams['toolbar'] = 'None'        # prepare image show
    plt.axis('off')                         # prepare image show
    note = message+"\n"+license             # init. the image note
    plt.title(note, fontsize=10)            # plot the image title
    plt.imshow(img)                         # plot the image
    plt.show(block=False)                   # show it
    plt.pause(delay)                        # pause for delay duration
    plt.close()                             # close the image plot

cfg_file.close()                            # close the text file...
```

##### Previous Knowledge

- basics of loops and branches
  
##### Learning Activities

1) read and understand the related text file
2) read the given Python code
3) write commands to read a text file
4) run the program
5) write a text file for a slide show

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
- read data from text files

[//]: # "learning objective: 1-files"
[//]: # "previous knowledge: 1-branch 1-loop"

*Complexity:*  2-normal

*Task type:*  completion task

---  
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2024  
License: CC BY-SA 4.0
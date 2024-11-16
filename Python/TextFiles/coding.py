file_name = 'MyEvent.txt'
event_file = open(file_name, 'r')             # open the text file 

while True:                                 # loop
    line = event_file.readline()     # read image file name
    line = line.strip()                     # remove line break 
    if line == '':                 # empty line -> stop reading
        break
    print(line)

event_file.close()

print()
add_data = input('Enter more guests (y/n)?')
if add_data == 'y':
    event_file = open(file_name, 'a')             # open the text file 
    while True:
        info = input('Guest information: ')
        if info == '':
            break
        event_file.write(info+'\n')

    event_file.close()


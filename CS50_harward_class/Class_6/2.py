#how to get data from file? See the different fns below:
def read1():
    with open("aa.txt", 'r') as file1: #loads the file in file handle 'file1'
        print(file1) #prints <_io.TextIOWrapper name='aa.txt' mode='r' encoding='cp1252'> which is in file1

#how to read the content in file?
def readfull_content():
    with open("aa.txt", 'r') as file2:
        print(file2.readlines())
readfull_content()

#default open as 'r'


#Reading Methods:

#read(size): Reads up to size bytes from the file.
#readline(): Reads a single line from the file.
#readlines(): Reads all the lines in the file and returns them as a list.

#Writing Methods:

#write(string): Writes a string to the file.
#writelines(list): Writes a list of strings to the file.

#File Navigation:

#seek(offset, whence): Moves the file cursor to a specific location.
#tell(): Returns the current position of the cursor in the file.
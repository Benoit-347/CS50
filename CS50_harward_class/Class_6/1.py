def w():
    a = input("enter str: ")
    open("aa.txt", 'w') #keyword open. open( <file_name>, <open type>)
    #opening in 'w' deletes prev data and if not exist, creates new
    file = open("aa.txt", 'w') #allows us to access the file after open (returns a file handle)
    file.write(a) #stores the data in var 'a' to file
    file.close() #Closing a file forces the buffer to flush, meaning all data is physically written to the file, ensuring data integrity
                #in some cases, due to buffering, changes made to a file may not show until you close the file.

#add data without removing old data?
def a():
    a = input("enter str: ")
    file = open("aa.txt", 'a') #adds the data to existing data in file
    file.write(f"{a}\n") 
    file.close()

#dont want to always give <file_handle>.close()? with open
def no_close():
    with open("aa.txt", 'w') as file:
        file.write("")
no_close()
#automatically handles closing the file, even if an error occurs.
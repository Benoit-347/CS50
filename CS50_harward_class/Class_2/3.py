#how to repeat for each element in data? 
data = [5, 6, 3]
for i in data: #takes a element in data
    print(i)
#works in string as well
for i in "hello":
    print(i)
print("end")
#you can also specify number of times to repeat in for loop:
#use range: returns a list of n numbers
for i in range(0 , 3, 1):#begin at 0(default), stop before 3(required), increment at 0(default)
    print(i)
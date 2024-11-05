#how to repeat for each element in data? 
#in takes characters present in a string or a certain value present in a list or tuple

data = [5, 6, 3]
for i in data: #takes a element in data
    print(i)

#note: a for loop only evaluates it's input once, at the beggining

#works in string as well
for i in "hello":
    print(i)
print("end")


#to specify number of times to repeat in for loop:
#use range: returns a list of n numbers

for i in range(0 , 3, 1):#begin at 0(default), stop before 3(required), increment at 0(default)
    print(i)

print("1:", list(range(0,7,-1)))
print("2:", list(range(7,0,-1)))
print("3:", list(range(-7,-1,-1)))
print("4:", list(range(-1,-7,-1)))
print("Enter number to check if it is a palindrome: ")
number = int(input("Enter number: "))
print(number)

number_reverse = 0
temp = number

# if the number is too long, the False the number of executions will be n times. To optimize this, we can find the total number of digits first, then run loop until num_digits/2
num_digits = len(str(number))

for i in range(num_digits//2):
    digit = temp %10
    temp = temp//10
    number_reverse = number_reverse *10 + digit
    print(f"The number {temp} reversed: {number_reverse}")
    if temp == number_reverse:
        print(f"{number} is a palindrome")
        break
else:
    digit = temp%10
    number_reverse = number_reverse*10 + digit
    print(f"The number {temp} reversed: {number_reverse}")
    if temp == number_reverse:
        print(f"{number} is a palindrome")
    else:
        print(f"The number {number} is not a palindrome")



# this above is very slow, use below instead:




# FASTER

if number < 0:
    print(f"{number} is not a palindrome")
elif number == 0:
    print(f"{number} is a palindrome")
else:
    # Optimization 1: Avoid math.log10 for speed and safety
    # Using len(str()) is highly optimized in Python
    num_digits = len(str(number))
    
    temp = number
    reverse = 0
    
    # Optimization 2: Run exactly half the iterations
    for _ in range(num_digits // 2):
        # Optimization 3: divmod calculates quotient and remainder in one step (faster in C)
        temp, digit = divmod(temp, 10)
        reverse = reverse * 10 + digit
        
    # Optimization 4: Simplified Check
    # If even length: temp == reverse
    # If odd length: temp == reverse // 10 (middle digit is now at the end of reverse)
    # Note: In your odd logic, the middle digit stays in 'temp', so we check 'temp // 10' against 'reverse'
    
    # For odd length (e.g. 121):
    # After loop: temp=12, reverse=1. (This approach requires different loop logic).
    
    # Let's stick to your specific "halfway" logic but corrected for the comparison:
    if num_digits % 2 == 1:
        # If odd, the middle digit is currently the last digit of 'temp'
        # We remove it to compare with 'reverse'
        temp = temp // 10
        
    if temp == reverse:
        print(f"{number} is a palindrome")
    else:
        print(f"The number {number} is not a palindrome")




# but using math method is much slower in python because it uses bytecode for each line, which has very high overhead per statement.

        # the str fn is very fast especially if the string is long as it will completely run in cypython
# FASTEST:
if number == int(str(number)[::-1]):
    print(f"Number {number} is a palindrome")
else:
    print(f"Number {number} is not a palindrome")
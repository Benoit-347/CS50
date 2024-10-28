def find_it(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
            
    for i in b:
        c = 0
        for j in a:
            if i == j:
                c += 1
        if c %2 ==1:
            return i
#time complexity n^2
# bad when all different or num in end
# for usual, bad when all different or num in end (worse when num repeated)
def find_it_gpt(arr):
    result = 0
    for num in arr:
        result ^= num #explain this#
    return result

def find_it_dict_gpt(arr):
    count_dict = {}

    # Count occurrences of each integer
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the integer that appears an odd number of times
    for num, count in count_dict.items():
        if count % 2 == 1:  # Check if the count is odd
            return num

    return None  # Return None if no odd occurrence is found

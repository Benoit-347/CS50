import random
#how to get a number (integer) from a range? (without a sequence)?
print(random.randint(1,2)) #including ceiling

#how to change positions of a sequence randomly? Shuffle
a = [5,2,3]
b = random.shuffle(a)
print(b)
#will it return value?
print(a)
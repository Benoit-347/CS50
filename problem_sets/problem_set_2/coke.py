due = 50

while due>0:
    print(f"Amount Due: {due}")
    cents = int(input("Insert Coin: "))
    
    if (cents == 25 or cents == 10 or cents ==5) :     # Allows only 25, 10, 5 denominators
        due = due - cents

print("Change Owed:", -due)

from datetime import date, timedelta

# 1. Define the starting date object
dob = date(1999, 1, 1)

# 2. Define the duration using the timedelta object
# 525,600 minutes is exactly 365 days
duration = timedelta(minutes=525600) 

# 3. Add the objects using the standard '+' operator
future_date = dob + duration

print(f"Start Date: {dob}")
print(f"Duration:   {duration}")
print(f"Future Date: {future_date}")
import pandas
titanic = pandas.read_csv("./Week_2/train.csv") # relative path, wrt the terminal path, which calls python execution.
                                                                            # (default terminal is the open folder path in vs code.

print(type(titanic))
print(f"\nThe head prints: \n{titanic.head()}")
print(f"\nThe description is: \n{titanic.describe()}")

"""
What the records of describe print- (The Output):

count  -> How many non-empty rows are in the column.
mean   -> The average value.
std    -> Standard Deviation (how spread out the numbers are).
min    -> The smallest value in the column.
25%    -> The 25th percentile (1/4 of data is below this value).
50%    -> The Median (the middle value).
75%    -> The 75th percentile (3/4 of data is below this value).
max    -> The largest value in the column.
"""

print("\nPrinting the titanic.info() fn:")
titanic.info()
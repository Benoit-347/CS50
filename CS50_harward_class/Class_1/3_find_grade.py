#For exclusive condition with flow along the seq?
#elif keyword is used when above is False then check if current is True
#exists the if seq when one of if/elif is True

#finding grade which lies in an interval:
score = int(input("Score: "))
#elif is skipped when is true and executed when if is false (it is vice versa with if)
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
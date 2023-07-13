leap_year=int(input("Enter the year:"))
leap_year=(leap_year%4==0 or leap_year%100!=0)and leap_year%400==0
if leap_year:
    print("The year is leap year")
else:
    print("The year is not leap year")
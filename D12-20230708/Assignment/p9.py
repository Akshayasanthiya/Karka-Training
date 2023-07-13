date=int(input("Weekday:"))
def day_calc(date):
    if date==0 or date==7:
        print("Today is a saturday")
    elif date==1:
        print("Today is a Sunday")
    elif date==2:
        print("Today is a monday")
    elif date==3:
        print("Today is a Tuesday")
    elif date==4:
        print("Today is a Wednesday")
    elif date==5:
        print("Today is a Thursday")
    elif date==6:
        print("Today is a Friday")
    else:
        print("error")
calc=day_calc(date)
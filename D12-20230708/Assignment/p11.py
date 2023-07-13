weight=int(input("Please enter your current earth weight:"))
print("\n")
print("I have information for the following planets:")
print("\t1.Venus\t\t2.Mars\t\t3.Jupiter\n\t4.Saturn\t5.Uranus\t6.Neptune")
print("\n")
planet=int(input("Which planet are you visiting?"))
print("\n")
def gravity(weight,planet):
    if planet==1:
        result=weight*0.78
    if planet==2:
        result=weight*0.39
    if planet==3:
        result=weight*2.65
    if planet==4:
        result=weight*1.17
    if planet==5:
        result=weight*1.05
    if planet==6:
        result=weight*1.23
    return result
calc=gravity(weight,planet)
print(f"Your weight would be {calc} pounds on that planet.")
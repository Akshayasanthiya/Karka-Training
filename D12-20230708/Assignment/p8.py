name=input("Hey, what's your name?")
age=int(input(f"Ok, {name}, how old are you?"))
def age_calc(name,age):
    if age<16:
        print(f"You can't drive,{name}")
    if age<18:
        print(f"You can't vote,{name}")
    if age<25:
        print(f"You can't rent a car,{name}")
    else:
        print(f"You can do anything that's legal,{name}")
calc=age_calc(name,age)

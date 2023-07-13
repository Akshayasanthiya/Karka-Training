name=input("Hello. What is your name?")
age=int(input(f"Hi, {name}! How old are You? "))
def age_calc(age):
        After_5yr=age+5
        Before_5yr=age-5
        return(f"Did you know that in five years you will be {After_5yr} years old? And five 
        years ago you were {Before_5yr}! Imagine that!")
calc=age_calc(age)
print(calc)

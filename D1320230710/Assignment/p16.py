gen=input("What is your gender (M or F):")
fname=input("First name:")
lname=input("Last name:")
age=int(input("Age:"))
if gen=="F" and age>=20:
    mar=input(f"Are you married, {fname}(y or n)?")
    if mar=="y":
        print(f"Mrs.{fname} {lname}")
    else:
        print(f"Ms. {fname} {lname}")
if gen=="F" and age<20:
    print(f"{fname} {lname}")
if gen=="M" and age>=20:
    print(f"Mr. {fname} {lname}")
if gen=="M" and age<20:
    print(f"{fname} {lname}")
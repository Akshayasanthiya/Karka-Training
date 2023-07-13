Item1=int(input("Enter the amount of Item1:"))
Item2=int(input("Enter the amount of Item2:"))
Item3=int(input("Enter the amount of Item3:"))
Item4=int(input("Enter the amount of Item4:"))
total=Item1+Item2+Item3+Item4
print(total)
if total>500 and total<1000:
    print("silver token")
if total>=1000:
    print("golden token")
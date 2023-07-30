num=int(input("Enter a number:"))
if num==1:
    print("The number is not a prime number.")
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("not a prime number.")
            break
    else:
        print("Is a prime number")

# num=int(input("Enter a number:"))
# if num==1:
#     print(f"{num} is not a prime number.")
# elif num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             print(f"{num} is not a prime number.")
#             # print(i,"times",num//i,"is",num)
#             break
#         else:
#             print(f"{num} is not a prime number.")
# else:
#     print(f"{num} is not a prime number")
num=int(input("Enter a number:"))
if num==1:
    print(num,"is not a prime number.")
elif num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number.")
            break
        
    else:
        print(num,"is a prime number.")
    
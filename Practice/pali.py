num=int(input("Enter a number:"))
Temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if (Temp==rev):
    print("The number is a palindrome.")
else:
    print("Not a palindrome.")
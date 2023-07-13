num1=int(input("Enter the number:"))
opr=input("Enter the operator:")
num2=int(input("Enter the number"))
def function(a,b,c):
    if b=="+":
        result = a+c
    elif b=="-":
        result = a-c
    elif b=="*":
        result = a*c
    elif b=="/":
        result = a/c
    elif b=="%":
        result = a%c
    elif b=="**":
        result = a**c
    else:
        return "Invalid operator"
    return result
calc=function(num1,opr,num2)
print(calc)
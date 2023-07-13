# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# s=(a+b+c)/2
# print(s)
# def tri(a,b,c,s):
#     Area=(s*(s-a)*(s-b)*(s-c))**0.5
#     return Area
# triangle=tri(a,b,c,s)
# print("Area of triangle:",triangle)

# a=int(input("Enter the value of a:"))
# def squ(a):
#     Area=a**2
#     return Area
# square=squ(a)
# print("Area of square:",square)

# r=int(input("Enter the value of r:"))
# def cir(r):
#     Area=3.14*r**2
#     return Area
# circle=cir(r)
# print("Area of circle:",circle)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
h=int(input("Enter h:"))
def trap(a,b,h):
    Area=((a+b)/2)*h
    return Area
trapezium=trap(a,b,h)
print("Area of Trapezium:",trapezium)
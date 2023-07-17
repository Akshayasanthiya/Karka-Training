frnds=[{"Name":"Akshaya","Age":20,"Place":"Theroor"},{"Name":"Vajeeha","Age":20,"Place":"Thittuvilai"},{"Name":"Abinaya","Age":21,"Place":"Vattavilai"},{"Name":"Valliammal","Age":21,"Place":"Krishnancoil"},{"Name":"Alfreena","Age":20,"Place":"STK"}]
n=frnds[0]
f1=frnds[1]
f2=frnds[2]
f3=frnds[3]
f4=frnds[4]
# print(n)
# for i in f1:
#     print(f"i am {f1["Name"]}, I am {f1["Age"]} years old, and I am from {f1["Place"]}")
# print(n["Name"])
print("I am ",n["Name"],", I am ",n["Age"]," years old, and I am from ",n["Place"],".")
print("I am ",f1["Name"],", I am ",f1["Age"]," years old, and I am from ",f1["Place"],".")
print("I am ",f2["Name"],", I am ",f2["Age"]," years old, and I am from ",f2["Place"],".")
print("I am ",f3["Name"],", I am ",f3["Age"]," years old, and I am from ",f3["Place"],".")
print("I am ",f4["Name"],", I am ",f4["Age"]," years old, and I am from ",f4["Place"],".")
for i,age in enumerate(frnds):
    a=(frnds[i]["Age"])
    print(a)
    if a>=21:
        print("Friends age greater than 21:\n",frnds[i])
    
    # if frnds["Age"]>=21:
    #     print(frnds["Name"]["Age"]["Place"])
friends=[{"Name":"Akshaya","Age":20,"Place":"Theroor"},{"Name":"Vajeeha","Age":20,"Place":"Thittuvilai"},{"Name":"Abinaya","Age":21,"Place":"Vattavilai"},{"Name":"Valliammal","Age":21,"Place":"Krishnancoil"},{"Name":"Alfreena","Age":20,"Place":"STK"}]
for a in friends:
    print(f'My name is {a["Name"]} and I am {a["Age"]} years old and from {a["Place"]}.')
    if a['Age']>=21:
        print("Age greater than 21",a)  

List=[{"Name":"Orange","Category":"Fruits"},{"Name":"Potato","Category":"Vegetables"},{"Name":"Grapes","Category":"Fruits"},{"Name":"Tomato","Category":"Vegetables"}]
Dict={"Fruits":[],"Vegetables":[]}
# Fruit=[]
# Vegetable=[]
for a in List:
    b=a['Category']
    c=a['Name']
    if b=='Fruits':
        Dict['Fruits'].append(c)
    if b=='Vegetables':
        Dict['Vegetables'].append(c)
# print("Fruits:",Fruit)
# print("vegetables:",Vegetable)
# Dict={"Fruits":Fruit,"Vegetbles":Vegetable}
print(Dict)

marks=[50,90,89,78,88]
total=0
# for mark in marks:
#     print("Before total:",total)
#     total+=mark
#     print("Total:",total)
enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enum_marks:
    print("Entering Iteration process for Item:"+str(i))
    print("Before sum",total)
    total+=mark
    print("After sum",total)
    print("Existing Iteration process for Item:"+str(i))
    print("\n")
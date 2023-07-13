l=[3,9,2,4,1,6,12,13,20,11]
even=[ ]
odd=[ ]
for num in l:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:",even)
print("Odd numbers:",odd)  
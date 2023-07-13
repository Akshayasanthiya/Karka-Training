print("WELCOME TO MITCHELL'S TINY ADVENTURE!")
print("\n")
qn1=input("You are in a creepy house! Would you like to go 'upstairs' or into the 'kitchen'?")
if qn1=="kitchen":
    qn2=input("There is a long countertop with dirty dishes everywhere. Off to one side there is, as you'd expect, a refrigerator. you may open the 'regrigerator' or look in a 'cabinet'")
    if qn2=="refrigerator":
        qn3=input("Inside the refrigerator you see food and stuff. It loooks pretty nasty.\n Would you like to eat some of the food?('yes or 'no)")
        if qn3=="yes":
            print("You have escaped!")
        if qn3=="no":
            print("You die of starvation")
    if qn2=="cabinet":
        qn4=input("Inside the cabinet you see fruits and some stuff.\n Would you like to eat fruits?(yes or no)")
        if qn4=="yes":
           print("You have escaped!")
        if qn4=="no":
            print("You die of starvation") 
if qn1=="upstairs":
    qn5=input("There is room in one side and other side there is balcony. \nWould you like to go to the room or balcony?")
    if qn5=="Room":
        qn6=input("There is a knife in the room.\n Will you take the knife?(yes or no)")
        if qn6=="yes":
            print("You have died")
        if qn6=="no":
            print("You have escaped")
    if qn5=="balcony":
        qn7=input("There is a plant in the balcony and there is flower from the plant.\n Would you like to take the flowers?(yes or no)")
        if qn7=="yes":
            print("You have died")
        if qn7=="no":
            print("You have escaped")            
    
        
        
    

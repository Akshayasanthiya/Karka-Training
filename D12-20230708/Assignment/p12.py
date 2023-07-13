ready=input("Are you ready for a quiz?")
a=0
if ready=="Y":
    print("Okay, here it comes!")
    quiz1=int(input("What is the capital of Alaska?\n\t1.Melbourne\n\t2.Anchorage\n\t3.Juneau\n"))
    if quiz1==3:
        print("That's right!")
        a+=1
    else:
        print(f"Sorry, {quiz1} is wrong.")
    quiz2=int(input('Can you store the value "cat" in a variable of type int?\n\t1.Yes\n\t2.No\n2'))
    if quiz2==2:
        print("That's right!")
        a+=1
    else:
        print(f"Sorry, {quiz2} is wrong.")
    quiz3=int(input("What is the result of 9+6/3?"))
    if quiz3==2:
        print("That's right!")
        a+=1
    else:
        print(f"Sorry, {quiz3} is wrong.")
    print(f"Overall, you got {a} out of 3 correct.")
    print("Thanks for playing")
else:
    print("Okay")
            


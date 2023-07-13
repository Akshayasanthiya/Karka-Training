print("TWO QUESTIONS!")
print("Think of an object, and I'll try to guess it.")
qn=input("Question 1) Is it animal, vegetable, or mineral?")
big=input("Question 2) Is it bigger than a breadbox?")
def check(qn,big):
    if qn=="animal" and big=="yes":
        print("My guess is that you are thinking of a mouse.\n aI would ask you if I'm right, but didn't actually care.")
    if qn=="animal" and big=="no":
        print("My guess is that you are thinking of a squirrel.\n I would ask you if I'm right, but didn't actually care.")
    if qn=="vegetable" and big=="yes":
        print("My guess is that you are thinking of a watermelon.\n I would ask you if I'm right, but didn't actually care.")
    if qn=="vegetable" and big=="no":
        print("My guess is that you are thinking of a carrot.\n I would ask you if I'm right, but didn't actually care.")
    if qn=="mineral" and big=="yes":
        print("My guess is that you are thinking of a camaro.\n I would ask you if I'm right, but didn't actually care.")
    if qn=="mineral" and big=="no":
        print("My guess is that you are thinking of a paper clip.\n I would ask you if I'm right, but didn't actually care.")
bread=check(qn,big)
    
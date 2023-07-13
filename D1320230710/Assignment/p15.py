print("TWO MORE QUESTIONS, BABY!")
print("Think of something and I'll try to guess it!")
qn1=input("Question 1) Does it stay inside or outside or both?")
qn2=input("Question 2) Is it a living thing?")
def ques(qn1,qn2):
    if qn1=="inside" and qn2=="yes":
        result="houseplant!"
        return result
    if qn1=="inside" and qn2=="no":
        result="shower curtain!"
        return result
    if qn1=="outside" and qn2=="yes":
        result="bison"
        return result
    if qn1=="outside" and qn2=="no":
        result="billboard"
        return result
    if qn1=="both" and qn2=="yes":
        result="dog"
        return result
    if qn1=="both" and qn2=="yes":
        result="cell phone"
        return result
check=ques(qn1,qn2)
print(f"Then what else could you be thinking of besides a {check}")

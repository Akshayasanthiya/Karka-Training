import p7
h=float(input("Enter your height:"))
w=int(input("Enter your weight:"))
bmi=p7.bmi_calc(h,w)
if bmi<18.5:
    print(f"your {bmi} is:Underweight")
if bmi>=18.5 and bmi<=24.9:
    print(f"your {bmi} is:normal weight")
if bmi>=25.0 and bmi<=29.9:
    print(f"your {bmi} is:overweight")
if bmi>=30.0:
    print(f"Your {bmi} is:obese")

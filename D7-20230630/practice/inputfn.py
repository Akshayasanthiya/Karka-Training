passed_out_yr=input("Which year you passed out from college:")
print(passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print(type_of_passed_out_yr)
passed_out_yr=int(passed_out_yr)
type_of_passed_out_yr=type(passed_out_yr)
print(type_of_passed_out_yr)
is_eligible=passed_out_yr>=2023 or passed_out_yr<=2026
if is_eligible:
    print("The student is eligible")
else:
    print("the student is not eligible")
s

year=int(input("Enter a year:"))
def check_eligibility(m):
    if m>2021 and m<=2023:
        return "The student is eligible"
    else:
        return "The student is not eligible"
is_eligible=check_eligibility(year)
print(is_eligible)
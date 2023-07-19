frnds=[{"Name":"Akshaya","Place":"Theroor","Hobbies":["Music","Webseries","Games"],"Marks":{"tamil":90,"english":92,"Maths":89,"Science":85,"social":87}},{"Name":"Alfreena","Place":"Then thamaraikulam","Hobbies":["Planting","webseries","games"],"Marks":{"tamil":91,"english":87,"Maths":85,"Science":80,"social":87}},{"Name":"Sharmila","Place":"Monday Market","Hobbies":["Cooking,Movies,Temple"],"Marks":{"tamil":93,"english":95,"Maths":98,"Science":85,"social":87}}]
for a in frnds:
    b=a['Marks']
    # print(b['tamil'])
    total=b['tamil']+b['english']+b['Maths']+b['Science']+b['social']
    print(a['Name'])
    print(f"Total SSLC marks of {a['Name']} is {total}")
    percent=(total/500)*100
    print(percent)
    if percent>90:
        print(f"{a['Name']} is eligible for Maths biology.")
    elif percent>80 and percent<90:
        print(f"{a['Name']} is eligible for Computer Science.")
    elif percent>75 and percent<80 and b['Maths']>=98:
        print(f"{a['Name']} is eligible for Maths Biology.")
    elif percent>70 and percent<75 and b['Maths']>=98:
        print(f"{a['Name']} is eligible for Computer Science.")
    # else:
    #     print("Nobody is eligible")
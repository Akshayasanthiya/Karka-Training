my_resume={"Name":"Akshaya.G.S."
,"E-mail":"akshayagopi03@gmail.com",
"Mobile No.":7010847020,
"Soft skills":["Communication","problem solving","Typing skill"],
"Hard skills":"Python",
"Qualification":[{"Course":"10th","Institute":"Isha Vidhya","Percent":88.6},{"Course":"12th","Institute":"Isha Vidhya","Percent":80},{"Course":"B.sc.Computer scisence","Institute":"WCC","Percent":89}],
"projects":[{"Topic":"Sleep Tracking app","Duration":"2 weeks","Description":"This app helps to track your sleep schedule"}],
"experience":[{"Company":"flow Global","Role":"Software developer","Duration":1},{"Company name":"Saama","Role":"App developer","Duration":2},{"Company name":"Karka","Role":"Intern","Duration":0.3}],
"Hobbies":["Music listening","Webseries"],
"Personal details":{"Father's name":"Gopi","Father's occupation":"Labour","Languages known":["Tamil","English","Malayalam"],"DOB":"02-04-2003","Gender":"Female","Marital Status":"Unmarried","Address":{"Door no.":"9/7","Street":"Vananthittu","Place":"Theroor"}}}
# print("Quslification:\n",my_resume['Qualification'])
# for a in my_resume:
#     b=a['Qualification']
#     print("Qualification:\n",b)
#     for i in b:
#         print(i)
#         print("Course:",i['Course'])
# for i in my_resume['Personal details']:
#     # print(i)
#     # print(my_resume[i])
#     print(f"{i}:{my_resume['Personal details'][i]}")
# for i in my_resume['Personal details']['Address']:
#     print(f"{i}:{my_resume['Personal details']['Address'][i]}")
# for i in my_resume['Personal details']:
#     print(f"{i}:{my_resume['Personal details']}")
#     if i=='Address':
#         for i in my_resume['personal details']:
#             print() 

        # print(f"{i}:{my_resume['Personal details']['Address'][i]}")
# for i in my_resume['projects']:
#     print(i)
#     print(i['Topic'])
for i in my_resume['Personal details']:
    if i=='Address':
        # print(my_resume['Personl details'][i])
        for j in my_resume['Personal details'][i]:
            print(f"{j}:{my_resume['Personal details']['Address'][j]}")
for i in my_resume['Personal details']:
    if i=='Languages known':
        for j in my_resume['Personal details'][i]:
            print(my_resume['Personal details']['Languages known']")
            
        

    
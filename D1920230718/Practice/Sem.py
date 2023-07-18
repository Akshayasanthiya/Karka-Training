Education_details=[{"Course":"B.Sc","Institue":"WCC","Semester marks":[{"sem":1,"Sub":["Tamil","English","Maths","C"],"Grade":"O"},{"sem":2,"Sub":["Tamil","English","C++","java"],"Grade":"A"}]}]
for sub in Education_details:
    a=sub['Semester marks']
    print(a)
    for i in a:
        print(i['Sub'])
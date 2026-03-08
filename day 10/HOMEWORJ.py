C = int(input("enter what celsius is out side: "))

if C > 30:
    print("ძალიან ცხელა!")
elif C > 20:
    print("სასიამოვნა ამინდია")
elif C > 10:
    print("ცოტა ცივა")
elif C > 0:
    print("ცივა ჩაიცვი თბილად")
else:
    print("გაიყინები, სახლში დარჩი!")


score = int(input("enter your score: "))
attendance = int(input("enter your attendance: "))

if score > 80 and attendance > 90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
elif score > 50 and attendance > 70:
    print("საშუალოდ დაწერე გამოცდა")
elif score > 30 and attendance > 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("შენ ჩაიჭერი")


    temp= int(input("enter temp: "))
    rain= bool(int(input("enter if its raining?(0-no , 1-yes): ")))
    if temp >20 and rain== False:
        print("შესანიშნავი ამინდია სასეირნოდ!")
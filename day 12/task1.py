math = int(input("enter your math score: "))
english = int(input("enter your english score: "))
physics = int(input("enter your physics score: "))

if math >= 90 and english >= 90 and physics>= 90:
    print("შესანიშნავი მოსწავლე ხარ")
    print("ყველა საგანში მაღალი შედეგი გაქვს")
elif math >= 70 and english >= 70 and physics >= 70:
    print("კარგი შედეგებია" )
    print("სასწავლო წელი წარმატებულია")
elif math <= 50 or english <= 50 or physics <= 50:
    print( "ერთ-ერთ საგანში დაბალი ქულა გაქვს"  )
    print("მეტი სწავლა დაგჭირდება")
else:
    print("შედეგები საშუალოა"  )
    print("შეგიძლია უკეთესიც")


age = int(input("enter your age: "))
license = bool(int(input("enter if you have license(0-no or 1-yes): ")))
drunk = bool(int(input("enter if you are drunk(0-no or 1-yes): ")))
if age >= 18 and license == True and drunk == False:
    print("შეგიძლია მანქანის მართვა")
    print("უსაფრთხო მგზავრობას გისურვებთ")
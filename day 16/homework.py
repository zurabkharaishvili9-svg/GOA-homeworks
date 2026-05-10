
for i in range(101):
    print(i)
for i in range(40, 251, 2):
    print(i)
for i in range(200, 400):
     if i % 2 == 0 and i % 5 == 0:
        print(i)
number = int(input("enter any number: "))
for i in range(2,number+1):
    print(i)
number1= int(input("enter any number: "))
for i in range(number1, -1, -1):
    print(i)

number = 7

guess = int(input("enter qny number: "))

while guess != number:
    if guess < number:
        print("უფრო დიდი რიცხვია")
    else:
        print("უფრო პატარა რიცხვია")

    guess = int(input("შეიყვანე რიცხვი: "))

print("გილოცავ! გამოიცანი ")
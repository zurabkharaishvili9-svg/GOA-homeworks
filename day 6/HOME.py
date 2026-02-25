
#input მაგალითია კლავიატურა მიკროფონი და კონტროლერი
#output კი ეკრანი დინამიკი და პრინტერი

Float = 2.6
INTEGER = 6
STR = "GOA" 

print(type(Float))
print(type(INTEGER))
print(type(STR))

KM = float(input("Distance from your home to school: "))
print(KM * 1000)

N1= int(input("Enter any number: "))
N2= int(input("Enter any number: "))
print(N1 + N2)
print(N2 - N1)
print(N2 / N1)
print(N1 // N2)
print(N1 * N2)
print(N2 ** N1)
print(N1 % N2)


name = input("Enter you name: ")

weight = int(input("Enter your weight in kg: "))

height = int(input("Enter your height in meters: "))

BMI = (weight * 703) / (height * height)

print(BMI)

print("Welcome to flw chart diag")
height=int(input("Please enter your height in cm "))
if height > 120:
    print("You are allowed in oyo")
    age = int(input("Please enter your age?"))
    if age > 19 and age < 25:
        print("Please pay 1000 rupees")
    elif age >= 25 and age < 45:
        print("Please pay 1500 rupees")
    else:
        print("Please pay 2000 rupees")
else:
    print("You are not allowed, Please dont come again!")

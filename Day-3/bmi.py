print("Welcome to BMI caliculator")
height=float(input("Enter your height in m: "))
weight=int(input("Enter your weight in kg: "))
bmi = weight/(height * height)
if bmi < 18.5:
  print(f"you are bmi is {bmi}, you are underweight")
elif bmi < 25:
  print(f"you are bmi is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"you are bmi is {bmi}, you are overweight")
elif bmi < 35:
  print(f"you are bmi is {bmi}, you are obese")
else:
  print(f"you are bmi is {bmi}, you are clinically obese")

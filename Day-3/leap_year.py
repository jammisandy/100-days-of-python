print("Welcome to leap year caliculator")
year=int(input("Enter the year: "))
if year % 4 != 0:
  print("Year is not leap year")
else:
  if year % 100 != 0:
    print("Year is leap year")
  else:
    if year % 400 == 0:
      print("Year is leap year")
    else:
      print("year is not leap year")

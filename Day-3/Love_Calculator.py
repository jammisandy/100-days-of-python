print("The Love Calculator is calculating your score...")
name1 = input("what is your name:") # What is your name?
name2 = input("What is their name:") # What is their name?
combined_name = name1 + name2
combined_string = combined_name.lower()
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
  print(f"your score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"your score is {love_score} , you are alright together")
else:
  print(f"your score is {love_score}.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
number = random.randint(1,100)
print(f"Pssst, the correct answer is {number}")
def easy():
  attempts = 10
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    else:
      print(f"You got it! The answer was {number}.")
      attempts = 0

def hard():
  attempts = 5
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    else:
      print(f"You got it! The answer was {number}.")
      attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  easy()

elif difficulty == "hard":
  hard()
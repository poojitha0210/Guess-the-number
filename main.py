from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

#---------------------------------------------
"""
from art import logo
import random
print(logo)
guess=random.randint(1,100)
print("Welcome to guessing game")
print("I am thinking of a number from 1 to 100 both inclusive")
choice=input("Select 'easy' or 'hard':\n")
c=0
count=10
while count>c:
  if choice=='easy':
    num=int(input("number:"))
    if guess==num:
      print(f"right answer the number is {guess}")
      break
    elif guess>num:
      print("too low")
      count-=1
      print(f"have {count} chances")
    elif guess<num:
      print("too high")
      count-=1
      print(f"have {count} chances")

  else:
    count=5
    while count>c:
      if choice=='hard':
        num=int(input("number:"))
        if guess==num:
          print(f"you won!\nRight answer the number is {guess}")
          break
        elif guess>num:
          print("too low")
          count-=1
          print(f"have {count} chances")
        elif guess<num:
          print("too high")
          count-=1
          print(f"have {count} chances")

print("Game over\nyou lost")  
"""
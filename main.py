#!/usr/bin/env python3

# Python Importing
import random

# Variables
user_score: int = 0
computer_score: int = 0
ties: int = 0
divider = "~"*50

# Start Menu
print(f'{divider}\nWelcome to the Rock Paper Scissors Game')
print(f"Start by entering one of the following: 'rock', 'paper', 'scissors'\n{divider}")

# Main Loop
while True:
  user_choice: str = str(input("Your Move - ")).lower()
  computer_choice: int = random.randint(0,2)
  if user_choice in ['end', 'quit']:
    print(f"{divider}\nYour Score - {user_score}")
    print(f"Computer Score - {computer_score}")
    print(f"Ties - {ties}\n{divider}")
    break
  elif user_choice not in ['rock', 'paper', 'scissors']:
    print("Enter one of the following: rock, paper, or scissors")
  else:
    if user_choice == 'rock':
      if computer_choice == 0:
        print("It is a tie.")
        ties += 1
      elif computer_choice == 1:
        print("Paper covers rock. You lose.")
        computer_score += 1
      elif computer_choice == 2:
        print("Rock crushes scissors. You win!")
        user_score += 1
    elif user_choice == 'paper':
      if computer_choice == 0:
        print("Paper covers rock. You win!")
        user_score += 1
      elif computer_choice == 1:
        print("It is a tie.")
        ties += 1
      elif computer_choice == 2:
        print("Scissors cuts paper. You lose.")
        computer_score += 1
    elif user_choice == 'scissors':
      if computer_choice == 0:
        print("Rock crushes scissors. You lose.")
        computer_score += 1
      elif computer_choice == 1:
        print("Scissors cuts paper. You win!")
        user_score += 1
      elif computer_choice == 2:
        print("It is a tie.")
        ties += 1
  print(divider)

import random

Number = random.randint(1,100)
Guess = input("Guess the number: ")

while not Guess.isdigit():
    Guess = input("This is not a number, please try again!: ")

while int(Guess) != Number:              
  if int(Guess) > Number:
                Guess = input("Your guess is too high! Try again: ")
                while not Guess.isdigit():
                    Guess = input("This is not a number, please try again!: ")
  elif int(Guess) < Number: 
                Guess = input("Your guess is too low! Try again: ")
                while not Guess.isdigit():
                    Guess = input("This is not a number, please try again!: ")
    
print("You are correct!")

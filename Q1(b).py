import random

computer_options = ["rock", "paper", "siccors"]
game = input("Enter rock, paper or scissors: ")
user = input("player chose:")
Computer = input("computer chose:")

computer_choice = computer_options [random.randint(0,2)]
if user == ("rock"):
    print("computer wins ")
elif user == ("paper"):
    print("player wins")
else:
    print("Draw")
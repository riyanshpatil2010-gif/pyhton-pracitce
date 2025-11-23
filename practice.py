#age = int(input("Enter your age: "))
#decades = age // 10
#yrs = age % 10
#print(f"You have lived for {decades} decades and {yrs} years.")

import random
user_input = input("Rodk paper or siccors: ")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")
if user_input == computer_choice:
    print("It's a tie!")
elif (user_input == "rock" and computer_choice == "scissors") or \
        (user_input == "paper" and computer_choice == "rock") or \
        (user_input == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")

import random

# Mapping for choices
choices = {"s": 1, "w": -1, "g": 0}
reverse_choices = {1: "Snake", -1: "Water", 0: "Gun"}

# Random choice by the computer
computer = random.choice([-1, 0, 1])  # -1 for Water, 0 for Gun, 1 for Snake

# User input
user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate user input
if user_input not in choices:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
else:
    user_choice = choices[user_input]
    print(f"You chose {reverse_choices[user_choice]}.")
    print(f"Computer chose {reverse_choices[computer]}.")

    # Game logic
    if computer == user_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer == -1) or (user_choice == -1 and computer == 0) or (user_choice == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")

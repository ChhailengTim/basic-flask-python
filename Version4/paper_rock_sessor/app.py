import random

exit_game = False
user_points = 0
computer_points = 0

while not exit_game:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ")
    
    if user_input == "exit":
        print("Game over!")
        exit_game = True
    elif user_input in options:
        computer_input = random.choice(options)

        print(f"Your input is {user_input}")
        print(f"Computer input is {computer_input}")

        if user_input == computer_input:
            print("It's a tie!")
        elif (
            (user_input == "rock" and computer_input == "scissors") or
            (user_input == "paper" and computer_input == "rock") or
            (user_input == "scissors" and computer_input == "paper")
        ):
            print("You win n!")
            user_points += 1
        else:
            print("Computer wins!")
            computer_points += 1
    else:
        print("Invalid input. Please choose rock, paper, scissors, or exit.")

print(f"Your points: {user_points}")
print(f"Computer points: {computer_points}")

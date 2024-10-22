# Programmers: Lucas Podowski
# Course:  CS151, Zelalem Yalew
# Due Date: 10/23/2024
# programming Assignment: 2
# Problem Statement: You are creating a three player game of the Game of Sticks.
# In this game there is a pile of sticks on the table, and players alternate turns taking 1-3 sticks.
# The player to take the last stick loses.
# Data In: initial number of sticks, sticks chosen
# Data Out: player1 losses, player 2 losses, computer losses

import random

# Loss counters for each player
player1_losses = 0
player2_losses = 0
computer_losses = 0

# outputs introductory statements
print('This game is called Sticks.\n'
      'There are two players and one computer.\n'
      'You lose the game if you take the last stick in the pile.\n')

# Initializes and continues the game until the user does not answer 'yes' to playing again
while True:
    # Gets the initial number of sticks from the user with error check
    while True:
        try:
            sticks = int(input("Enter the initial number of sticks you want on the table (between 10 and 100): "))
            if 10 <= sticks <= 100:
                break
            else:
                print("Please enter a number between 10 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    current_player = 1  # Start with Player 1

    # Loops the game until all sticks are taken
    while sticks > 0:
        print(f"\nThere are {sticks} sticks on the table.") # Displays number of sticks on the table

        if current_player == 1:
            # Player 1's turn and error checks for their sticks taken
            while True:
                try:
                    sticks_chosen = int(input("Player 1, how many sticks will you take (1, 2, or 3)? "))
                    if sticks_chosen in [1, 2, 3]:
                        break # Ends player 1's turn
                    else:
                        print("You must take 1, 2, or 3 sticks.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif current_player == 2:
            # Player 2's turn and error checks for their sticks taken
            while True:
                try:
                    sticks_chosen = int(input("Player 2, how many sticks will you take (1, 2, or 3)? "))
                    if sticks_chosen in [1, 2, 3]:
                        break # Ends player 2's turn
                    else:
                        print("You must take 1, 2, or 3 sticks.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        else:
            # Generates a random number of sticks for the computer's turn
            sticks_chosen = random.randint(1, 3)
            print(f"The computer takes {sticks_chosen} sticks.")

        # Subtract the sticks taken from the total
        sticks -= sticks_chosen

        # Checks which player took the last stick adding a loss to their counter.
        if sticks <= 0:
            if current_player == 1:
                print("Player 1 has taken the last stick and loses!")
                player1_losses += 1
            elif current_player == 2:
                print("Player 2 has taken the last stick and loses!")
                player2_losses += 1
            else:
                print("The computer has taken the last stick and loses!")
                computer_losses += 1
            break

        # Move to the next player (Player 1 -> Player 2 -> Computer -> Player 1)
        current_player = (current_player % 3) + 1

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    # Ends the game if their answer is not yes
    if play_again != 'yes':
        break

# Displays the loss statistics for each player including the computer
print("\nGame Over! Here are the results:\n"
      f"\tPlayer 1 losses: {player1_losses}\n"
      f"\tPlayer 2 losses: {player2_losses}\n"
      f"\tComputer losses: {computer_losses}\n\n"
      "-----Thank You for Playing!!!-----")



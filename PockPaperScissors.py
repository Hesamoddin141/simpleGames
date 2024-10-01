import random

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Main function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate player input
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    # Computer's random choice
    computer_choice = random.choice(choices)
    
    # Display choices
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Call the game function
if __name__ == "__main__":
    play_game()

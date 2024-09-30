''' A complex system that works is invariably found to have evolved from a simple system that worked 
_ John Gall  '''

import random

# this function will make a number between 10 to 99 randomly and return a list with 2 member
def secret_number() -> list[int]:
    # Generate a random secret number with more than one digit
    secret_number = random.randint(10, 99)  # Generate a random number between 10 and 99
    # Convert the random number to a list of digits by make it str and the one by one int
    TheNumber = [int(digit) for digit in str(secret_number)]  
    return TheNumber


# this function will get inputs as guess from user
def user_guess() -> list[int]:
    while True:
        try:
            guess = input("Guess the secret number (between 10 and 99): ")
            guess_number = int(guess)
            if 10 <= guess_number <= 99:
                guess_digits = [int(digit) for digit in str(guess_number)]
                return guess_digits
            else:
                print("Your guess is outside the valid range (10-99). Please notice the range.")
        except ValueError:
            print("Invalid input! Please enter a valid number (10-99).")


# the main function that made of 2 loop 
def play_game() -> None:
    print("\nWelcome to The Secret Number Game!")
    play_again = True #making a varable that can be operate like switch to break loop with user input
    
    # outer loop 
    while play_again:
        TheNumber = secret_number()  # calling secret_number function 
        print("\nA secret number has been chosen. Try to guess it!")
        attempts = 0 #the first attemps
        # inner loop 
        while True:
            guess_digits = user_guess()  # calling user_guess function 
            attempts += 1  # counting attempts
            
            #compare user input with the secret number
            if guess_digits == TheNumber:
                print(f"\nCongratulations! You guessed the secret number {TheNumber} in {attempts} attempts.")
                break
            else:
                #checking length of input
                if len(guess_digits) != 2:
                    print("\nYour guess should be a two-digit number. Please try again.")
                else:
                    if guess_digits[0] < TheNumber[0]:
                        print("\nYour guess is too low try more.")
                    elif guess_digits[0] > TheNumber[0]:
                        print("\nYour guess is too high try lower numbers.")
                    else:
                        if guess_digits[1] < TheNumber[1]:
                            print("\nYou are getting there, but it is low.")
                        elif guess_digits[1] > TheNumber[1]:
                            print("\nYour guess is good,but high.")
    
        play_again_input = input("\nDo you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            play_again = False # beark the loop by turning value of the outer loop to False
            
    print("\nThank you for playing The Secret Number Game!")

# Start the game by calling the main function
play_game()

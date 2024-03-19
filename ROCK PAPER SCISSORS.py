
import random

def get_user_choice():
    while True:
        s = input("Enter your choice (ROCK, PAPER, SCISSORS): ").upper()
        if s in ["ROCK", "PAPER", "SCISSORS"]:
            return s
        else:
            print("Invalid input. Please enter ROCK, PAPER, or SCISSORS.")
            print()

def get_computer_choice():
    return random.choice(["ROCK", "PAPER", "SCISSORS"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (user_choice == "PAPER" and computer_choice == "ROCK") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    n = 3
    user_wins = 0
    computer_wins = 0
    
    print("YOU HAVE THREE CHANCES TO PLAY")
    print()
    
    for _ in range(n):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_wins += 1
        elif result == "You lose!":
            computer_wins += 1
            
    print("OVERALL RESULT")        
    
    if user_wins > computer_wins:
        print("YOU WIN")
    elif user_wins == computer_wins:
        print("DRAW MATCH")
    else:
        print("YOU LOST")

play_game()

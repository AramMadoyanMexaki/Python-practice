import random
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    while user_choice not in ["rock", "paper", "scissors"]:
        print("It was a wrong choice, choose rock, paper or scissors.")
        user_choice = input("Enter your choice: ")

    return user_choice

def get_computer_choice():
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    return computer_choice

def check_winner():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    if user_choice == computer_choice:
        print(f"No one! The computer made the choice {computer_choice}. Try again.")
    elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
        print(f"You won! The computer made the choice {computer_choice}")
    else:
        print(f"Computer won! The computer made choice {computer_choice}")

def play_or_not():
    answer = str(input("Are you want to play again ? Y(yes)/N(no) "))
    if answer == 'Y' or answer == 'y':
        game()
    elif answer == 'N' or answer == 'n':
        print("Okay. Thanks for playing.")

def game():
    print("Welcome to Chinga-Chung game")
    check_winner()
    play_or_not()

game()
import random  # Importing the random module to generate random numbers

# Print instructions for the game
print("Rock VS Paper => Paper Wins")
print("Rock VS Scissors => Rock Wins")
print("Paper VS Scissors => Scissors wins")
print("If you have x life, you have to win x times against the computer\n")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors\n")

# Function to prompt the user for the number of lives they want for the game
def game_life():
    while True:
        try:
            life = int(input("How many lives do you want to have? : "))
            return life
        except ValueError:
            print("Error, Please enter a number !!!")
            continue

# Function to implement the game logic for Rock, Paper, Scissors
def rock_paper_scissors(life):
    words = ["rock", "paper", "scissors"]  # List of possible choices
    your_score = 0  # Initialize player's score
    computer_score = 0  # Initialize computer's score

    # Loop for the number of lives specified by the user
    for i in range(life):
        while True:
            # Prompt the user for their choice and validate it
            choice = input(f"Choice {i + 1}: ")
            if choice.lower() in words:
                break
            else:
                print("Error, you can enter only rock, paper, or scissors !!!")
                continue

        # Generate a random choice for the computer
        computer_number = random.randint(1, 3)
        computer_choice = words[computer_number - 1]  # Translate the computer number to its corresponding choice

        print("The computer chooses:", computer_choice)

        # Determine the winner of the round based on the choices
        if computer_choice == "rock" and choice.lower() == "paper":
            print("You win!!!")
            your_score += 1  # Increment player's score
            print()
        elif computer_choice == "paper" and choice.lower() == "scissors":
            print("You win!!!")
            your_score += 1  # Increment player's score
            print()
        elif computer_choice == "scissors" and choice.lower() == "rock":
            print("You win!!!")
            your_score += 1  # Increment player's score
            print()
        elif computer_choice == choice.lower():
            print("It's a tie!")
            print()
        else:
            print("You lose!")
            computer_score += 1  # Increment computer's score
            print()

    # Print final scores and determine the winner of the game
    print("Your score:", your_score)
    print("Computer's score:", computer_score)
    if your_score > computer_score:
        print("You're the winner !!!")
        print()
    elif computer_score > your_score:
        print("The computer is the winner !!!")
        print()
    else:
        print("It's a tie !!!")
        print()

    # Prompt the user if they want to play again
    while True:
        choice1 = input("Wanna try again? yes or no : ")
        if choice1.lower() == "yes":
            life = game_life()
            rock_paper_scissors(life)
            break
        elif choice1.lower() == "no":
            print("Goodbye !!!")
            break
        else:
            print("Error !!!")
            continue

# Main program logic
life = game_life()  # Get the number of lives from the user
rock_paper_scissors(life)  # Start the game with the specified number of lives


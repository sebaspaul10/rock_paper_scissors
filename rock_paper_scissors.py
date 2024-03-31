import random

print("Rock VS Paper => Paper Wins")
print("Rock VS Scissors => Rock Wins")
print("Paper VS Scissors => Scissors wins")
print("If you have x life, you have to win x times against the computer\n")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors\n")

def game_life():
    while True:
        try:
            life = int(input("How many lives do you want to have? : "))
            return life
        except ValueError:
            print("Error, Please enter a number !!!")
            continue

def  rock_paper_scissors (life):

    words = ["rock", "paper", "scissors"]
    your_score = 0
    computer_score = 0

    for i in range(life):
        while True:
            choice = input(f"Choice {i + 1}: ")
            if choice.lower() in words:
                break
            else:
                print("Error, you can enter only rock, paper, or scissors !!!")
                continue
        
        computer_number = random.randint(1, 3)
        computer_choice = words[computer_number - 1]  # Translate the computer number to its corresponding choice

        print("The computer chooses:", computer_choice)

        if computer_choice == "rock" and choice.lower() == "paper":
            print("You win!!!")
            your_score =  your_score + 1
            print()
        elif computer_choice == "paper" and choice.lower() == "scissors":
            print("You win!!!")
            your_score =  your_score + 1
            print()
        elif computer_choice == "scissors" and choice.lower() == "rock":
            print("You win!!!")
            your_score =  your_score + 1
            print()
        elif computer_choice == choice.lower():
            print("It's a tie!")
            print()
        else:
            print("You lose!")
            computer_score  = computer_score + 1
            print()

    print (your_score)
    print(computer_score)

    if your_score > computer_score:
        print ("You're the winner !!!")
        print()
    if computer_score > your_score:
        print ("The computer is the winner !!!")
        print()
    if your_score == computer_score:
        print ("It's a  tie !!!")
        print()
    
    while True:
        choice1 = input ("Wanna  try again ? yes or no : ")
        if choice1.lower() == "yes":
            life = game_life()
            rock_paper_scissors(life)
            break
        elif choice1.lower() == "no":
            print ("Goodbye !!!")
            break
        else:
            print ("Error !!!")
            continue

life = game_life()
rock_paper_scissors(life)

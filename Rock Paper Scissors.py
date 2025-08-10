# Side Prtoject Day 4
rock = "*this is a rock image"
paper = "*this is a paper image"
scissors = "this is a scissor image"

import random
bot_choices = [rock, paper, scissors]
print(input("Welcome to Rock,Paper,Scissors v. Python. . ."))
answer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if answer == "0":
    print(input(f"You chose Rock [0].{rock}"))
    print(input("The bot draw a. . . "))
    bot_choice = random.choice(bot_choices)
    print(f"A {bot_choice}")
    if bot_choice == bot_choices[0]:
        print("Tied")
        exit()
    elif bot_choice == bot_choices[1]:
        print("You Lose, Womp womp")
        exit()
    elif bot_choice == bot_choices[2]:
        print("You Win")
        exit()
    else:
        print("Invalid answer please try again.")
        exit()
elif answer == "1":
    print(input(f"You chose Paper [1].{paper}"))
    print(input("The bot draw a. . . "))
    bot_choice = random.choice(bot_choices)
    print(f"A {bot_choice}")
    if bot_choice == bot_choices[0]:
        print("You Win")
        exit()
    elif bot_choice == bot_choices[1]:
        print("Tied")
        exit()
    elif bot_choice == bot_choices[2]:
        print("You Lose, Womp womp")
        exit()
    else:
        print("Invalid answer please try again.")
        exit()
else:
    print(input(f"You chose Scissors [2].{scissors}"))
    print(input("The bot draw a. . . "))
    bot_choice = random.choice(bot_choices)
    print(f"A {bot_choice}")
    if bot_choice == bot_choices[0]:
        print("You Lose, Womp womp")
        exit()
    elif bot_choice == bot_choices[1]:
        print("You Win")
        exit()
    elif bot_choice == bot_choices[2]:
        print("Tied")
        exit()
    else:
        print("Invalid answer please try again.")
        exit()

'''# -*- coding: utf-8 -*-'''
import random as r

def startgame():
    lives = 5
    while True:
        computer_no = r.randint(0,99)
        
        health = '❤ '
        print("Computer Pick Random Number between 0 to 99 🤖")
        print(f"\n\t\tLives: {health*lives}")
        guess_no = int(input("\n🔢 Your Guess NO:"))

        if guess_no == computer_no:
            print("You Won ✌🏻")
            break
        elif guess_no < computer_no:
            print("You Guess Low ⏳")
            
        elif guess_no > computer_no:
            print("You Guess High ⌛")
        lives = lives-1    
        
        if lives == 0:
            print("Game Over ❌")
            print("All Lives Are finished")
            print("Try Again .. Next Time")
            break


while True:
    print("\n\n\n====== Number Guessing Game 🔢 ======")
    print("\n💡 Description :\n This Game Chooses a Random Number between 0 and 99 and Gives 5 Lives")

    print("\n1.Start Game\n2.Exit")
    choice = int(input("Enter The Choice:"))

    if choice == 1:
        startgame()
    elif choice == 2:
        break
import random
from time import sleep


def welcome():
    print("*                  WELCOME                       *")
    print("*   Rock(✊) - Paper(🖐) - Scissors(✌)   *")
    print("\nThe rules of the game are:\n- Paper wins against Rock.\n- Rock wins against Scissor.\n- Scissor wins against paper.\nThe player and computer will both pick a play and whoever chose the winning play is the winner.\n")

def play():
    player = input("Press r for Rock(✊), p for Paper(🖐) or s for Scissors(✌)\n: ").lower()
    plays = ["r","p","s"]
    while len(player) > 1 or player not in plays:
        player = input("Invalid choice, please select either r for Rock or p for Paper or s for Scissors\n: ").lower()
    computer = random.randint(0,2)
    sleep(1)
    match player:
        case "r":
            if computer == 0:
                print("Player: Rock(✊)\nComputer: Rock(✊)")
                sleep(1)
                print("It's a tie")
            elif computer == 1:
                print("Player: Rock(✊)\nComputer: Paper(🖐)")
                sleep(1)
                print("Computer wins!😡")

            else:
                print("Player: Rock(✊)\nComputer: Scissors(✌)")
                sleep(1)
                print("Player wins😁")

        case "p":
            if computer == 0:
                print("Player: Paper(🖐))\nComputer: Rock(✊)")
                sleep(1)
                print("Player wins😁")

            elif computer == 1:
                print("Player: Paper(🖐)\nComputer: Paper(🖐)")
                sleep(1)
                print("It's a tie\n")
            else:
                print("Player: Paper(🖐)\nComputer: Scissors(✌)")
                sleep(1)
                print("Computer wins!😡")

        case "s":
            if computer == 0:
                print("Player: Scissors(✌)\nComputer: Rock(✊)")
                sleep(1)
                print("Computer wins!😡")

            elif computer == 1:
                print("Player: Scissors(✌)\nComputer: Paper(🖐)")
                sleep(1)
                print("Player wins😁")

            else:
                print("Player: Scissors(✌)\nComputer: Scissors(✌)")
                sleep(1)
                print("It's a tie")



running = True

welcome()

while running:
    play()
    play_again = input("Do you want to play again? \nPress Yes(y) or No(n):  ").lower()

    if play_again == "y" or play_again == "yes":
        running = True
    elif play_again == "n" or play_again == "no":
        running = False
    else:
        print("Invalid input!\nGoodbye")
        sleep(1)
        break
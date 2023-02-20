import random

def dice_sum(a, b):
    return a + b

def game():
    goal = 0
    flag = True
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"The sum of dice is {dice1} + {dice2} = {dice_sum(dice1, dice2)}")
    if dice_sum(dice1, dice2) == 7 or dice_sum(dice1, dice2) == 11:
        print("Congratulations!!! You WON.")
    elif dice_sum(dice1, dice2) == 2 or dice_sum(dice1, dice2) == 3 or dice_sum(dice1, dice2) == 12:
        print("I'm sorry, you lost.")
    else:
        goal = dice_sum(dice1, dice2)
        print(f"Now your goal is {goal}.")
        while flag:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"The sum of dice is {dice1} + {dice2} = {dice_sum(dice1, dice2)}")
            if dice_sum(dice1, dice2) == goal:
                print("You won.")
                flag = False
            elif dice_sum(dice1, dice2) == 7:
                print("You lose.")
                flag = False

answer = input("Do you want to start the game?(yes/no): ")
if answer.lower() == "yes":
    game()
    again = input("Do you want to play again?(yes/no): ")
    while again.lower() == "yes":
        game()
        again = input("Do you want to play again?(yes/no): ") 
    if again.lower() == "no":
        print("Thank you for participation.")
else:
    print("Your loss.")

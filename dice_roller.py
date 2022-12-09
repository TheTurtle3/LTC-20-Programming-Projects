import random

def roll_dice():
    dice_drawing = {
        1: (
            "+-------+",
            "|       |",
            "|   O   |",
            "|       |",
            "+-------+",
        ),
        2: (
            "+-------+",
            "| O     |",
            "|       |",
            "|     O |",
            "+-------+",
        ),
        3: (
            "+-------+",
            "| O     |",
            "|   O   |",
            "|     O |",
            "+-------+",
        ),
        4: (
            "+-------+",
            "| O   O |",
            "|       |",
            "| O   O |",
            "+-------+",
        ),
        5: (
            "+-------+",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            "+-------+",
        ),
        6: (
            "+-------+",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            "+-------+",
        ),
    }
    
    roll = input("Roll the dice? (Yes/No): ")
    while roll.lower() == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("dice rolled: {} and {}".format(dice1, dice2))

        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/No): ")

roll_dice()
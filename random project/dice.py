import random

# function and stuff
def parse_input():
    # get the input and validate the input
    global num_dice_input
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    if num_dice_input in {"1", "2", "3", "4", "5", "6"}:
        return int(num_dice_input)
        #loop back again if the input isnt between 1 and 6
    else:
        print("The input has to be in between 1 and 6, Try again")
        return parse_input()
def rattled(num_dice):
    result = []
    for i in range(num_dice):
        result.append(random.randint(1, 6))
    return result
# main code goes here
#1. Get the ammount of dice
num_dice = parse_input()
#2. Roll the damm thing
roll_result = rattled(num_dice)

print(roll_result)

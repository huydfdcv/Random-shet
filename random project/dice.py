import random
def parse_input():
    num_dice_input = input("How many dice do you want to roll? [1-6]")
    return int(num_dice_input) if num_dice_input in {"1", "2", "3", "4", "5", "6"} else parse_input()
def rattled(fnum_dice, result=[]):
    for i in range(fnum_dice): result.append(random.randint(1, 6))
    return result
print(rattled(parse_input()))

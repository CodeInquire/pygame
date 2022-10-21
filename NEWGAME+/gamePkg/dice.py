
def diceRoll(sideCount):
    import random
    match sideCount:
        case 2:
            print(random.choice(range(1, 3)))
        case 4:
            print(random.choice(range(1, 5)))
        case 6:
            print(random.choice(range(1, 7)))
        case 8:
            print(random.choice(range(1, 9)))
        case 10:
            print(random.choice(range(1, 11)))
        case 20:
            roll = random.choice(range(1, 21))
            print('CRITICAL') if roll == 20 else print(roll)
        case 100:
            print(random.choice(range(1, 101)))

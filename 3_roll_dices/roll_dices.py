'''
Program outline:
    - user inputs a number of dices to roll.
        - user input != int:
            - print 'Enter a number: ' and ask for input.
        - user input == int:
            - print 'Rolling...'.
            - sleep for 5 ms.
            - the program prints a random number between 1 and 6.
            - back to print 'Rolling...'.
'''

import random
import time

def get_no_dice():
    try:
        no_dice = int(input('Enter a number of dice and receive that many rolls: '))
    except ValueError:
        return
    
    return no_dice

def main():
    no_dice = get_no_dice()

    while no_dice is None:
        no_dice = get_no_dice()

    dice = random.choices(range(1,7), k=no_dice)

    for d in dice:
        print('Rolling...')
        time.sleep(0.5)
        print(d)

if __name__ == '__main__':
    main()
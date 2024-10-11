'''
Program outline:
    - user asked for input between 1 and 10
    - user input wrong:
        - out of range -> ask for input again
        - not a number -> ask for input again
    - user input correct:
        - guess is correct -> show 'Your guess for <number> is correct!'
        - guess is wrong -> ask for input again
'''

def get_guess():

    try:
        guess = int(input('Guess the number between 1 and 10: '))
    except ValueError:
        return
    
    return guess if 1 <= guess <= 10 else None

def main():
    winner = 5
    guess = 0
    
    while guess != winner:
        guess = get_guess()

    print(f'Your guess for {guess} is correct!')


if __name__ == '__main__':
    main()
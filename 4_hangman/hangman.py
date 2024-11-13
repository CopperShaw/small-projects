'''
Program outline:
    1. User is presented with the hidden word.
    2. User is asked to type a letter.
    3. Program check if letter is in word and responds accordingly.
        3.1 Letter in word: Display the hidden word + guessed letters + ask for input if word not completely guessed and tries > 0.
        3.2 Letter not in word: Display the hidden word + ask for input + decrease tries.
        3.3 Input not a letter: Ask for input again.
'''
import random

def get_input_letter():
    letter = input('Guess a letter: ')

    if isinstance(letter, str):
        return letter
    
    return None

def main():
    words = ['banana', 'apple', 'sauce']
    chosen_word = random.choice(words)

    tries = len(chosen_word)
    good_guesses = ''

    while tries > 0:
        print('Word: ', end=' ')
        for letter in chosen_word:
            if letter in good_guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()
        
        guess = get_input_letter()
        if guess in chosen_word:
            if guess not in good_guesses:
                good_guesses += guess
            else:
                print(f'You already guessed {guess}')
        else:
            tries -=1
            print(f'Wrong guess, {tries} tries remaining!')



if __name__ == '__main__':
    main()
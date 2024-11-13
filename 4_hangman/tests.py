'''
Tests:
    - Test input is a letter +!.
    - Test correct letter works +!.
    - Test tries behaviour: good guesses leave tries, bad guesses decrease tries.
'''

from hangman import get_input_letter

def test_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'a')
    inp = get_input_letter()
    # ensures strings work as input
    assert inp == 'a'

    monkeypatch.setattr('builtins.input', lambda _:27)
    inp = get_input_letter()
    # ensures non strings don't work as input
    assert inp is None

def test_correct_letter(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _:'a')
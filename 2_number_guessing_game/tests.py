'''
Tests:
    - input is in range
    - input is a number
    - correct guess wins

I try to create test for condition and  !condition in the same function.
i.e. test_correct_guess will test both cases when guess correct and when not correct
'''

from guess_the_number import get_guess, main

def test_n_in_range(monkeypatch):

    # test n in range
    monkeypatch.setattr('builtins.input', lambda _:4)
    result = get_guess()

    assert result == 4

    # test n out of range
    monkeypatch.setattr('builtins.input', lambda _:11)
    result = get_guess()

    assert result == 'Enter a number between 1 and 10: '

def test_n_is_number(monkeypatch):

    # test n is number already done abone

    # test n is not a number
    monkeypatch.setattr('builtins.input', lambda _:'Test')
    result = get_guess()

    assert result == 'Enter a number between 1 and 10: '

def test_guess_is_correct(monkeypatch, capsys):

    # test correct guess
    monkeypatch.setattr('builtins.input', lambda _:5)
    result = get_guess()
    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == 'Your guess for 5 is correct!'

    # couldn't find a way to test incorrect guess as main would be stuck asking for input
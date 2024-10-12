'''
Tests:
    - test user input == int
    - test number of rolls == requested n of rolls
    - test rolls between 1 and 6
'''
import re
from roll_dices import get_no_dice, main

def test_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:2)
    inp = get_no_dice()

    assert inp == 2

    monkeypatch.setattr('builtins.input', lambda _:'Two')
    inp = get_no_dice()

    assert inp is None

def test_no_rolls(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _:2)
    get_no_dice()
    main()

    captured = capsys.readouterr()
    clean_captured = captured.out.strip()

    returned_no_dice = re.findall(r'\d+', clean_captured)

    assert len(returned_no_dice) == 2
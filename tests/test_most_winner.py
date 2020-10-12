import pytest
import most_winner

def test_get_most_winner_player_1():
    games = [('Mark', 10), ('Tom', 90), ('Albert', 23)]
    assert most_winner.get_most_winner_player(games) == ('Tom', 90)

def test_get_most_winner_player_2():
    games = []
    assert most_winner.get_most_winner_player(games) == None

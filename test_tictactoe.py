import tictactoe
import io
import pytest

def test_check_end_game():
    assert tictactoe.check_end_game([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert tictactoe.check_end_game(["X", "X", "X", 4, 5, 6, 7, 8, 9]) == True
    assert tictactoe.check_end_game(["X", "X", "O", 4, 5, 6, 7, 8, 9]) == False
    assert tictactoe.check_end_game([1, 2, 3, "X", "X", "X", 7, 8, 9]) == True
    assert tictactoe.check_end_game(["X", "O", "X", 4, 5, 6, 7, 8, 9]) == False
    assert tictactoe.check_end_game([1, 2, 3, 4, 5, 6, "X", "X", "X"]) == True
    assert tictactoe.check_end_game(["O", "O", "O", 4, 5, 6, 7, 8, 9]) == True
    assert tictactoe.check_end_game([1, 2, 3, "O", "O", "O", 7, 8, 9]) == True
    assert tictactoe.check_end_game([1, 2, 3, 4, 5, 6, "O", "O", "O"]) == True
    assert tictactoe.check_end_game(["X", 2, 3, "X", 5, 6, "X", 8, 9]) == True
    assert tictactoe.check_end_game([1, "X", 3, 4, "X", 6, 7, "X", 9]) == True
    assert tictactoe.check_end_game([1, 2, "X", 4, 5, "X", 7, 8, "X"]) == True
    assert tictactoe.check_end_game(["O", 2, 3, "O", 5, 6, "O", 8, 9]) == True
    assert tictactoe.check_end_game([1, "O", 3, 4, "O", 6, 7, "O", 9]) == True
    assert tictactoe.check_end_game([1, 2, "O", 4, 5, "O", 7, 8, "O"]) == True
    assert tictactoe.check_end_game(["X", 2, 3, 4, "X", 6, 7, 8, "X"]) == True
    assert tictactoe.check_end_game([1, 2, "X", 4, "X", 6, "X", 8, 9]) == True
    assert tictactoe.check_end_game(["O", 2, 3, 4, "O", 6, 7, 8, "O"]) == True
    assert tictactoe.check_end_game([1, 2, "O", 4, "O", 6, "O", 8, 9]) == True
    assert tictactoe.check_end_game([1, 2, "X", 4, 5, 6, 7, 8, 9]) == False

def test_get_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("1"))
    assert tictactoe.get_input("X", [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    monkeypatch.setattr("sys.stdin", io.StringIO("a\n2"))
    assert tictactoe.get_input("X", [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n2"))
    assert tictactoe.get_input("X", ["X", 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    monkeypatch.setattr("sys.stdin", io.StringIO("0\n2"))
    assert tictactoe.get_input("X", [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    monkeypatch.setattr("sys.stdin", io.StringIO("10\n2"))
    assert tictactoe.get_input("X", [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", io.StringIO("10"))
        tictactoe.get_input("X", [1, 2, 3, 4, 5, 6, 7, 8, 9])



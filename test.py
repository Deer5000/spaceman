# test function
from Spaceman import *

def test_is_word_guessed():
	assert is_word_guessed("word", "word") == True
	assert is_word_guessed("sad", "solid") == False
	assert is_word_guessed("circle", "circle") == True
	assert is_word_guessed("round", "round") == True


def test_letter_in_word():
	assert letter_in_word("v", "benevolence") == True
	assert letter_in_word("g", "glad") == True
	assert letter_in_word("s", "screen") == True
	assert letter_in_word("m", "look") == False

def test_get_guessed_word():
	assert get_guessed_word("get", ["g","t"]) == ["g","_","t"], "works great!"
	assert get_guessed_word("lamp", ["l","a","p"]) == ["l","a","_","p"], "works great!"
	assert get_guessed_word("bad", ["b","a"]) == ["b","a","_"], "works great!"
	assert get_guessed_word("spin", ["s","i","n"]) == ["s","_","i","n"], "works great!"

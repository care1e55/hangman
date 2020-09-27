import sys
import logging
# import io
sys.path.append('./hangman')
from hangman import Hangman

logging.basicConfig(filename="test.log", level=logging.INFO)
logger = logging.getLogger(__name__) 
hang = Hangman()

# def test_hang():
#     hang = Hangman()
#     hang.play("Hello", 5)

def test_hide_word():
    word = "test"
    mask = "****"
    logger.info(f'Testing hide_word with {word} and {mask}')
    assert "".join(hang.hide_word(word)) == mask

def test_find_indexes():
    word = "test"
    letter = "t"
    indexes = [0,3]
    logger.info(f'Testing find_indexes with {word}, {letter} and {indexes}')
    assert hang.find_indexes(letter, word) == indexes

def test_reveal():
    hidden = "****"
    letter = "t"
    indexes = [0,3]
    unmasked = "t**t"
    logger.info(f'Testing reveal with {hidden}, {letter}, {indexes} and {unmasked}')
    assert "".join(hang.reveal(list(hidden), indexes, letter)) == unmasked

def test_gues():
    mistakes_count, hidden = hang.gues("t", "test", ["*", "*", "*", "*"], 0, 5)
    assert mistakes_count == 0
    assert "".join(hidden) == "t**t"

def test_mistake():
    mistakes_count, hidden = hang.gues("x", "test", ["*", "*", "*", "*"], 0, 5)
    assert mistakes_count == 1
    assert "".join(hidden) == "****"

import sys
import logging
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
    logger.info("Testing hide_word with {word} and {mask}")
    assert "".join(hang.hide_word(word)) == mask

def test_find_indexes():
    word = "test"
    letter = "t"
    indexes = [0,3]
    logger.info("Testing find_indexes with {word}, {letter} and {indexes}")
    assert hang.find_indexes(letter, word) == indexes

def test_reveal():
    hidden = "****"
    letter = "t"
    indexes = [0,3]
    unmasked = "t**t"
    logger.info("Testing reveal with {hidden}, {letter}, {indexes} and {}")
    assert "".join(hang.reveal(list(hidden), indexes, letter)) == unmasked

def test_gues():
    pass




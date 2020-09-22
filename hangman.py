import re

class Hangman():
    def __init__(self):
        pass

    @staticmethod
    def hide_word(word):
        return list("*"*len(word))

    @staticmethod
    def reveal(hidden, found_indexes, letter):
        for i in found_indexes:
            hidden[i] = letter
        return hidden
    
    def find_indexes(self, letter, word):
        return [i.start() for i in re.finditer(letter, word)]

    def gues(self, letter, word, hidden, mistakes_count, max_mistakes):
        found_indexes = self.find_indexes(letter, word)
        if found_indexes:
            print("Hit!")
            hidden = self.reveal(hidden, found_indexes, letter)
        else:
            mistakes_count += 1
            print("Missed, mistake {} out of {}".format(mistakes_count, max_mistakes))
        print("The word: {}".format("".join(hidden)))
        return mistakes_count, hidden

    def play(self, word, max_mistakes = 5):
        hidden = self.hide_word(word)
        word = word.lower()
        mistakes_count = 0
        while (mistakes_count != max_mistakes) and ("".join(hidden) != word):
            mistakes_count, hidden = self.gues(str(input()).lower(), word, hidden,  mistakes_count, max_mistakes)
        if "".join(hidden) == word:
            print("You won!")
        else:
            print("You lost!")


if __name__ == "__main__":
    hang = Hangman()
    hang.play("Hello", 5)
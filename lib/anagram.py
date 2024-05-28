from collections import Counter

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted(word)
        self.word_count = Counter(self.word_letters)

    def match(self, word_list):
        match_word_list = [word for word in word_list if sorted(word) == sorted(self.word_letters) and Counter(word) == self.word_count]

        return match_word_list
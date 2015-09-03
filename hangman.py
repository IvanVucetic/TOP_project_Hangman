from linecache import getline
from random import randint

dict_ = open('5desk.txt')
num_lines = sum(1 for line in dict_)


word = ""

# gets specific line from a file
while (5 >= len(word)) or (len(word) >= 12):
    word = getline('5desk.txt', randint(1, num_lines))
    # need to remove trailing space so it doesn't affect word's length
    word = str.strip(word)

print word, len(word)


# preparing the game

correct_letters = "_" * len(word)   # to display correctly guessed letters
empty_slots = len(word) # unguessed letters; game ends when == 0 (all guessed)
incorrect_letters = []  # display incorrect guesses to avoid repeating them
attempts_left = 6   # TODO: turn into a gallows
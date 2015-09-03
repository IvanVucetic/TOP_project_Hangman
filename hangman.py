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
empty_slots = len(word)  # unguessed letters; game ends when == 0 (all guessed)
incorrectly_guessed = []  # display incorrect guesses to avoid repeating them
correctly_guessed = []  # take note of previous guesses
attempts_left = 6   # TODO: turn into gallows

while True:
    
    print correct_letters
    print "Incorrect attempts: ", incorrectly_guessed
    print "Attempts left: ", attempts_left

    print "Guess new letter:"
    new_attempt = raw_input("> ")
    print "new attempt: ", new_attempt

    if new_attempt in correctly_guessed:
        print "You have guessed this letter already, try another."

    elif new_attempt in incorrectly_guessed:
        print "You have already tried this one."

    else:
        if new_attempt in word:
            print "Bravo!"
            correctly_guessed.append(new_attempt)
            # change correct_letters to show position of guessed letter
            # empty_slots = empty_slots - num of letter occurences in a word
            if empty_slots == 0: 
                print "---"
                print "You have WON!!!"
                break
        
        else:
            print "Wrong...!"
            incorrectly_guessed.append(new_attempt)
            attempts_left -= 1
            if attempts_left == 0: 
                print "---"
                print "You have lost... :("
                break
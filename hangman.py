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

# display correctly guessed letters
letters_position = []
for i in range(len(word)):
    letters_position.append("_")

# word into a list for indexing purposes
word_list = list(word)

empty_slots = len(word)  # unguessed letters; game ends when == 0 (all guessed)
incorrectly_guessed = []  # display incorrect guesses to avoid repeating them
correctly_guessed = []  # take note of previous guesses
attempts_left = 6   # TODO: turn into gallows

while True:
    
    print "".join(letters_position)  # print string, not list
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
            
            # change letters_position to show position of guessed letter
            for i in range(word.count(new_attempt)):
                index = word_list.index(new_attempt)
                letters_position[index] = new_attempt
                # ne mozemo da pop-ujemo iz word_list jer to menja indexe
                word_list[index] = "_"

            empty_slots = empty_slots - word.count(new_attempt)
            if empty_slots == 0: 
                print "---"
                print "You have WON!!!"
                print "---"
                break
        
        else:
            print "Wrong...!"
            incorrectly_guessed.append(new_attempt)
            attempts_left -= 1
            if attempts_left == 0: 
                print "---"
                print "You have lost... :("
                print "---"
                break
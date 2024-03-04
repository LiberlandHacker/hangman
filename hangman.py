# Problem Set 2, hangman.py
# Name: Jonathan A. McCormick, Jr.
# Collaborators:
# Time spent: 6h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_input_permitted(entry):
    '''
    Returns True if the character is an English letter, and an Error if it is not.
    '''
    permitted_chars = string.ascii_lowercase

    if len(entry) != 1:
        return "Error: Input must be a single character."
    entry = entry.lower()
    if entry in permitted_chars:
        return True
    else:
        return "Error: Input must be an English letter."


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_ "
    return guessed_word


def set_of_unique_chars_in_word(word):
    ''' 
    word: string
    returns: set of unique characters in word.
    '''
    unique_chars = set()  # Initialize an empty set
    for char in word:
        unique_chars.add(char)  # Add char to the set, duplicates will be ignored
    return unique_chars



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    length_of_secret_word = len(secret_word)
    # print("Length of secret word: " + str(length_of_secret_word))
    unique_chars_of_secret_word = set_of_unique_chars_in_word(secret_word)
    number_of_guesses = 6
    ran_out_of_guesses = False
    number_of_warnings = 3
    ran_out_of_warnings = False
    letters_correctly_guessed = []
    letters_incorrecly_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(length_of_secret_word) +
          " letters long.")
    # Create a loop here to play the game until resolution.
    while ran_out_of_guesses == False and ran_out_of_warnings == False:
        user_guess = input("You have " + str(number_of_guesses) +
                           " guesses and " + str(number_of_warnings) +
                           " warnings left.\nPlease enter a letter: ").lower()

        # Validate the user's entry
        if is_input_permitted(user_guess) != True:
            print(is_input_permitted(user_guess))
            number_of_warnings -= 1
            

        if user_guess in unique_chars_of_secret_word:
            letters_correctly_guessed.append(user_guess)
            print("Good guess! " +
                  get_guessed_word(secret_word, letters_correctly_guessed)
                  )  # Verify this line later
        else:
            letters_incorrecly_guessed.append(user_guess)
            number_of_guesses -= 1

            print("Oops! That letter is not in my word: " +
                  get_guessed_word(secret_word, letters_correctly_guessed))

        # User has guessed the word correctly.
        if is_word_guessed(secret_word, letters_correctly_guessed):
            print("Congratulations, you won!")
        # User has run out of guesses.
        if number_of_guesses <= 0:
            print("!" * 10 + "\nSorry, you ran out of guesses. The word was " + secret_word + ".")
            ran_out_of_guesses = True
        if number_of_warnings <= 0:
            print("!" * 10 + "\nSorry, you ran out of warnings. The word was " + secret_word + ".")
            ran_out_of_warnings = True


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    print("#"*30 + "\n" + "\nSecret word is: " + secret_word + "\n"*2 + "#"*30)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)

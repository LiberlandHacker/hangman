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
permitted_chars = string.ascii_lowercase


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
    print(f"  {len(wordlist)} words loaded.")
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


def is_entry_ascii_lower(entry):
    '''
    Returns True if entry is lowercase ASCII, otherwise returns False.
    '''
    if entry in permitted_chars:
        return True
    else:
        return False


def has_len_1(entry):
    '''
    Returns True if entry is 1 character long, otherwise returns False.
    '''
    if len(entry) == 1:
        return True
    else:
        return False


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
        unique_chars.add(
            char)  # Add char to the set, duplicates will be ignored
    return unique_chars


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = set()
    for char in permitted_chars:
        if char not in letters_guessed:
            available_letters.add(char)
    return "".join(sorted(available_letters))


def warning_decrement(num_of_guesses, num_of_warnings):
    '''
    num_of_guesses: int, number of guesses left
    num_of_warnings: int, number of warnings left
    returns: tuple of two ints, first being the number of guesses left after decrementing
             by 1 if necessary, and the second being the number of warnings left after
             decrementing by 1.
    '''
    if num_of_warnings > 0:
        num_of_warnings -= 1
        print(f"You have {num_of_warnings} warnings left.")
    else:
        num_of_guesses -= 1
        print("You have no warnings left, so you lose one guess.")
    return num_of_guesses, num_of_warnings


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
    length_of_secret_word = len(secret_word)
    unique_chars_of_secret_word = set_of_unique_chars_in_word(secret_word)
    number_of_guesses = 6
    number_of_warnings = 3
    game_over = False
    letters_correctly_guessed = set()  # Initialize empty set
    letters_incorrectly_guessed = set()  # Initialize empty set
    print(
        f"Welcome to the game Hangman!\nI am thinking of a word that is {length_of_secret_word} letters long."
    )

    # Create a loop here to play the game until resolution.
    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} guesses left and {number_of_warnings} warnings left.")
        available_letters = get_available_letters(
            letters_correctly_guessed.union(letters_incorrectly_guessed))
        print(f"Available letters: {available_letters}")
        user_guess = input("Please enter a letter: ").lower()

        # Validate the user's entry

        if is_entry_ascii_lower(user_guess):
            if has_len_1(user_guess):
                if user_guess not in letters_incorrectly_guessed and user_guess not in letters_correctly_guessed:
                    if user_guess in unique_chars_of_secret_word:
                        print("Good job! You guessed correctly!")
                        letters_correctly_guessed.add(user_guess)
                    else:
                        print(
                            f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_correctly_guessed)}"
                        )
                        letters_incorrectly_guessed.add(user_guess)
                        number_of_guesses -= 1  # REPLACE WITH ACTUAL FUNCTION
                else:
                    # Example usage within the hangman function
                    number_of_guesses, number_of_warnings = warning_decrement(
                        number_of_guesses, number_of_warnings)
                    print(
                        f"Oops! You've already guessed that letter. You now have {number_of_guesses} guesses and {number_of_warnings} warnings left."
                    )
            else:
                # Example usage within the hangman function
                number_of_guesses, number_of_warnings = warning_decrement(
                    number_of_guesses, number_of_warnings)

                print(
                    "Oops! You've entered more than one character, or no character at all."
                )
        else:
            # Example usage within the hangman function
            number_of_guesses, number_of_warnings = warning_decrement(
                number_of_guesses, number_of_warnings)

            print(
                "Oops! You've entered an invalid character. Please enter an ASCII lowercase letter."
            )

        # Determine if the user wins or loses

        # User WINS: has guessed the word correctly.
        if is_word_guessed(secret_word, letters_correctly_guessed):
            print("Congratulations, you won!")
            break  # Game won, exit the loop

        if number_of_guesses <= 0:  # Check if no guesses left
            print(
                f"Sorry, you ran out of guesses. The word was '{secret_word}'."
            )
            break  # No guesses left, exit the loop


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
    print("#" * 30 + "\n" + "\nSecret word is: " + secret_word + "\n" * 2 +
          "#" * 30)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)

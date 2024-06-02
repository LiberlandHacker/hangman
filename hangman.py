# Problem Set 2, hangman.py
# Name: Jonathan A. McCormick, Jr.
# Collaborators: Replit, ChatGPT
# Time spent: 10h

# Hangman Game
# NOTE: I have personally taken the liberty to not be limited by the assignment in a strict sense, but have nonetheless fulfilled the spirit of it, if not the letter of it.
import os  # Needed for clearing the console
import random
import string

WORDLIST_FILENAME = "words.txt"
permitted_chars = string.ascii_lowercase


def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS, Linux/Unix
    else:
        _ = os.system('clear')


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


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_entry_ascii_lower(entry):
    '''
    Returns True if entry is lowercase ASCII, otherwise returns False.
    '''
    entry in permitted_chars  # Yes, this is correct syntax.


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all(char in letters_guessed for char in secret_word)


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


def hangman_figure(guesses_left):
    states = [
        # Final state: head, torso, both arms, and both legs
        """
           ------
           |    |
           |    💀
           |   \\|/
           |    |
           |   / \\
          ---
        """,
        # State 5: head, torso, both arms, and one leg
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   /
          ---
        """,
        # State 4: head, torso, and both arms
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   
          ---
        """,
        # State 3: head, torso, and one arm
        """
           ------
           |    |
           |    O
           |   \\|
           |    |
           |   
          ---
        """,
        # State 2: head and torso
        """
           ------
           |    |
           |    O
           |    |
           |    |
           |   
          ---
        """,
        # State 1: head
        """
           ------
           |    |
           |    O
           |    
           |    
           |   
          ---
        """,
        # State 0: initial empty state
        """
           ------
           |    |
           |    
           |    
           |    
           |   
          ---
        """
    ]
    return states[6 - guesses_left]


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, one potential matching word
    returns: boolean, True if all actual letters of my_word match the corresponding
             letters of other_word and that other_word does not contain any letters
             that are already revealed in my_word
    '''
    my_word = my_word.replace(" ", "")  # Remove spaces from guessed word
    if len(my_word) != len(other_word):
        return False

    for (my_char, other_char) in zip(my_word, other_word):
        if my_char != "_" and my_char != other_char:
            return False
        if my_char == "_" and other_char in my_word:
            return False

    return True


def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: nothing, but should print out every word in wordlist that matches my_word and
             does not contain any letters that are not in the secret word.
    '''
    # Extract letters from my_word that are guessed correctly
    correct_letters = set([char for char in my_word if char != '_'])
    # Determine incorrect letters from letters guessed
    incorrect_letters = [
        char for char in letters_guessed if char not in correct_letters
    ]

    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word) and not any(char in incorrect_letters
                                                      for char in word):
            matches.append(word)

    if matches:
        print("Possible word matches are:")
        print(" ".join(matches))
    else:
        print("No matches found.")


def hangman_with_hints(secret_word):
    length_of_secret_word = len(secret_word)
    number_of_guesses = 6
    number_of_warnings = 3
    letters_guessed = set()

    while number_of_guesses > 0:
        clear_screen()
        print(
            f"Welcome to the game Hangman!\nI am thinking of a word that is {length_of_secret_word} letters long."
        )
        print(hangman_figure(6 - number_of_guesses))
        print(
            f"You have {number_of_guesses} guesses left and {number_of_warnings} warnings left."
        )
        print("Available letters:", get_available_letters(letters_guessed))
        print("Current guessed word:",
              get_guessed_word(secret_word, letters_guessed))

        guess = input("Please enter a letter, or '*' for a hint: ").lower()

        if guess == "*":
            show_possible_matches(
                get_guessed_word(secret_word, letters_guessed),
                letters_guessed)
            input("Press enter to continue...")  # Wait for user input

        elif guess in letters_guessed:
            number_of_guesses, number_of_warnings = warning_decrement(
                number_of_guesses, number_of_warnings)
            print(
                f"You've already guessed that letter. You now have {number_of_warnings} warnings left."
            )
        elif guess in permitted_chars and len(guess) == 1:
            letters_guessed.add(guess)
            if guess in secret_word:
                print("Good guess: ",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                number_of_guesses -= 1
                print("Oops! That letter is not in my word:",
                      get_guessed_word(secret_word, letters_guessed))
        else:
            number_of_guesses, number_of_warnings = warning_decrement(
                number_of_guesses, number_of_warnings)
            print("Invalid entry. Please enter a lowercase English letter.")

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break

        if number_of_guesses <= 0:
            clear_screen()
            print(
                f"End of the game Hangman!\nI was thinking of a word that is {length_of_secret_word} letters long."
            )
            print(hangman_figure(6))
            print(
                f"You have {number_of_guesses} guesses left and {number_of_warnings} warnings left."
            )
            print("Available letters:", get_available_letters(letters_guessed))
            print("Current guessed word:",
                  get_guessed_word(secret_word, letters_guessed))
            print("Sorry, you ran out of guesses. The word was \"" +
                  secret_word + "\".")
            break  # No guesses left, exit the loop


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

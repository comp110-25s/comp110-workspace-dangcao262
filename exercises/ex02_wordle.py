""" Wordle exercise """

__author__ = "730747262"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""

    turn = 1

    guess = ""

    while turn <= 6 and guess != secret:
        print(f"===Turn {turn}/6===")
        guess = input_guess(expected_length=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
        turn += 1
    if turn >= 6:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, single_letter: str) -> bool:
    """a function that checks for "single_letter" in "word" by indexing through"""

    assert len(single_letter) == 1, f"len('{single_letter}') is not 1"

    index = 0

    while index < len(word):
        if word[index] == single_letter:
            return True
        index += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """a function that implements colored emojis into the program based on input"""

    assert len(guess_word) == len(secret_word), "Guess must be same length as secret"

    reveal = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index = 0

    while index < len(secret_word):
        if contains_char(word=secret_word, single_letter=guess_word[index]):
            if guess_word[index] == secret_word[index]:
                reveal += GREEN_BOX
            else:
                reveal += YELLOW_BOX
        else:
            reveal += WHITE_BOX
        index += 1
    return reveal


def input_guess(expected_length: int) -> str:
    """checks to make sure the guessed word by the user is of appropriate length"""
    n_guess = input(f"Enter a {expected_length} Character word: ")

    while len(n_guess) != expected_length:
        n_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return n_guess


if __name__ == "__main__":
    main(secret="codes")

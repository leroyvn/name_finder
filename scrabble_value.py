import argparse
import unicodedata


# Letter values (French Scrabble)
_VALUE_TO_LETTER = {
    1: list("eainorstul"),
    2: list("dmg"),
    3: list("bcp"),
    4: list("fhv"),
    8: list("jq"),
    10: list("kwxyz")
}


def test_letters():
    # Check if no letter is missing and no letter is added more than once
    all_letters = []
    for letters in _VALUE_TO_LETTER.values():
        all_letters.extend(letters)
    all_letters.sort()
    print(all_letters)
    assert all_letters == list("abcdefghijklmnopqrstuvwxyz")


# Assign its value to each letter
_LETTER_TO_VALUE = {
    letter: value
    for value, letters in _VALUE_TO_LETTER.items()
    for letter in letters
}


def normalize(s):
    s = s.lower()
    return "".join((c for c in unicodedata.normalize("NFD", s)
                    if unicodedata.category(c) != "Mn"))


def test_normalize():
    # Test if the normalisation routine works as intended
    assert normalize("áàâäçéèêëíìîïñóòôöúùûü") == "aaaaceeeeiiiinoooouuuu"


def scrabble_value(word):
    """Compute the value of a word.

    Parameters:
        word (``str``): Word whose value is to be computed.

    Returns -> ``int``:
        Word value.
    """
    word = normalize(word)
    value = 0
    for letter in word:
        value += _LETTER_TO_VALUE[letter]

    return value


def cli(args):
    print(scrabble_value(args.word))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word")
    args = parser.parse_args()
    cli(args)

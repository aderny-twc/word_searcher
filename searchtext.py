import string


def search4letters(phrase:str, letters:str='aeiou') -> set:
    """
    Returns a set of letters from 'letters' that are found in 'phrase'.
    """
    return set(letters).intersection(set(phrase))


def search4words(text:str, words:str) -> set:
    """
    Returns a set of words from 'words' that are found in 'text'.
    """

    def word_abs(phrase:str) -> list:
        """
        Returns a list of words in lowercase.
        """
        clean_phrase = phrase.translate(str.maketrans('', '', string.punctuation))
        return [word.lower() for word in clean_phrase.split()]

    return set(word_abs(words)).intersection(word_abs(text))

"""
Character conversion utilities for different languages.
This module provides various character conversion functions that can be used
across multiple projects for converting characters from various languages to English equivalents.
"""

from collections.abc import Callable

_GREEK_TO_ENGLISH: dict[str, str] = {
    "Α": "A",
    "Ά": "A",
    "Β": "B",
    "Γ": "G",
    "Δ": "D",
    "Ε": "E",
    "Έ": "E",
    "Ζ": "Z",
    "Η": "I",
    "Ή": "I",
    "Θ": "TH",
    "Ι": "I",
    "Ί": "I",
    "Ϊ": "I",
    "Κ": "K",
    "Λ": "L",
    "Μ": "M",
    "Ν": "N",
    "Ξ": "X",
    "Ο": "O",
    "Ό": "O",
    "Π": "P",
    "Ρ": "R",
    "Σ": "S",
    "Τ": "T",
    "Υ": "Y",
    "Ύ": "Y",
    "Ϋ": "Y",
    "Φ": "F",
    "Χ": "CH",
    "Ψ": "PS",
    "Ω": "O",
    "Ώ": "O",
    "α": "a",
    "ά": "a",
    "β": "b",
    "γ": "g",
    "δ": "d",
    "ε": "e",
    "έ": "e",
    "ζ": "z",
    "η": "i",
    "ή": "i",
    "θ": "th",
    "ι": "i",
    "ί": "i",
    "ϊ": "i",
    "ΐ": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ξ": "x",
    "ο": "o",
    "ό": "o",
    "π": "p",
    "ρ": "r",
    "σ": "s",
    "ς": "s",
    "τ": "t",
    "υ": "y",
    "ύ": "y",
    "ϋ": "y",
    "ΰ": "y",
    "φ": "f",
    "χ": "ch",
    "ψ": "ps",
    "ω": "o",
    "ώ": "o",
}

# Capital letters whose Latin form has two letters. "TH" is right inside an
# all-capitals word (ΑΘΗΝΑ -> ATHINA) but wrong at the start of a normal one
# (Θεσσαλονίκη -> Thessaloniki), so the case of the second letter depends on the
# neighbours.
_GREEK_CAPITAL_DIGRAPHS: dict[str, str] = {"Θ": "TH", "Χ": "CH", "Ψ": "PS"}
# The pair ου is written "ou" (Παπαδόπουλος -> Papadopoulos), not "oy".
_GREEK_OMICRON: frozenset[str] = frozenset("οόΟΌ")
_GREEK_UPSILON: dict[str, str] = {"υ": "u", "ύ": "u", "Υ": "U", "Ύ": "U"}


def convert_greek_characters_to_english(text: str) -> str:
    """
    Transliterate Greek letters (with or without tonos) to Latin letters.

    Letter by letter, close to the Greek standard ELOT 743 for single letters:
    η is "i" (Θεσσαλονίκη -> Thessaloniki), ου is "ou" (Παπαδόπουλος ->
    Papadopoulos), and Θ, Χ, Ψ give "Th", "Ch", "Ps" unless they stand in an
    all-capitals word (ΑΘΗΝΑ -> ATHINA). The other letter pairs ELOT treats
    specially (αυ, ευ, μπ, γγ, ...) are not handled.

    Args:
        text: Text containing Greek characters

    Returns:
        Text with Greek characters converted to Latin letters
    """
    result: list[str] = []
    for index, char in enumerate(text):
        preceding = text[index - 1] if index > 0 else ""
        if char in _GREEK_UPSILON and preceding in _GREEK_OMICRON:
            result.append(_GREEK_UPSILON[char])
            continue
        digraph = _GREEK_CAPITAL_DIGRAPHS.get(char)
        if digraph is None:
            result.append(_GREEK_TO_ENGLISH.get(char, char))
            continue
        following = text[index + 1] if index + 1 < len(text) else ""
        in_capitals_word = following.isupper() or (
            not following.isalpha() and preceding.isupper()
        )
        result.append(digraph if in_capitals_word else digraph.capitalize())
    return "".join(result)


def convert_swedish_characters_to_english(text: str) -> str:
    """
    Convert Swedish characters to English equivalents.

    Args:
        text: Text containing Swedish characters

    Returns:
        Text with Swedish characters converted to English equivalents
    """
    swedish_to_english_mapping: dict[str, str] = {
        "Å": "A",
        "å": "a",
        "Ä": "A",
        "ä": "a",
        "Ö": "O",
        "ö": "o",
        "É": "E",
        "é": "e",
        "È": "E",
        "è": "e",
        "Ü": "U",
        "ü": "u",
        "Ñ": "N",
        "ñ": "n",
        "Ç": "C",
        "ç": "c",
    }

    return "".join(swedish_to_english_mapping.get(char, char) for char in text)


def convert_german_characters_to_english(text: str) -> str:
    """
    Convert German characters to English equivalents.

    Args:
        text: Text containing German characters

    Returns:
        Text with German characters converted to English equivalents
    """
    german_to_english_mapping: dict[str, str] = {
        "Ä": "Ae",
        "ä": "ae",
        "Ö": "Oe",
        "ö": "oe",
        "Ü": "Ue",
        "ü": "ue",
        "ß": "ss",
        "É": "E",
        "é": "e",
        "È": "E",
        "è": "e",
        "À": "A",
        "à": "a",
        "Ò": "O",
        "ò": "o",
        "Ù": "U",
        "ù": "u",
    }

    return "".join(german_to_english_mapping.get(char, char) for char in text)


def convert_french_characters_to_english(text: str) -> str:
    """
    Convert French characters to English equivalents.

    Args:
        text: Text containing French characters

    Returns:
        Text with French characters converted to English equivalents
    """
    french_to_english_mapping: dict[str, str] = {
        "Æ": "Ae",
        "æ": "ae",
        "Œ": "Oe",
        "œ": "oe",
        "À": "A",
        "à": "a",
        "Á": "A",
        "á": "a",
        "Â": "A",
        "â": "a",
        "Ä": "A",
        "ä": "a",
        "Ç": "C",
        "ç": "c",
        "É": "E",
        "é": "e",
        "È": "E",
        "è": "e",
        "Ê": "E",
        "ê": "e",
        "Ë": "E",
        "ë": "e",
        "Î": "I",
        "î": "i",
        "Ï": "I",
        "ï": "i",
        "Ô": "O",
        "ô": "o",
        "Ö": "O",
        "ö": "o",
        "Ù": "U",
        "ù": "u",
        "Ú": "U",
        "ú": "u",
        "Û": "U",
        "û": "u",
        "Ü": "U",
        "ü": "u",
        "Ÿ": "Y",
        "ÿ": "y",
    }

    return "".join(french_to_english_mapping.get(char, char) for char in text)


def convert_spanish_characters_to_english(text: str) -> str:
    """
    Convert Spanish characters to English equivalents.

    Args:
        text: Text containing Spanish characters

    Returns:
        Text with Spanish characters converted to English equivalents
    """
    spanish_to_english_mapping: dict[str, str] = {
        "Á": "A",
        "á": "a",
        "É": "E",
        "é": "e",
        "Í": "I",
        "í": "i",
        "Ó": "O",
        "ó": "o",
        "Ú": "U",
        "ú": "u",
        "Ñ": "N",
        "ñ": "n",
        "Ü": "U",
        "ü": "u",
    }

    return "".join(spanish_to_english_mapping.get(char, char) for char in text)


def no_conversion(text: str) -> str:
    """
    No-op character conversion function.
    Returns the text unchanged.

    Args:
        text: Input text

    Returns:
        Text unchanged
    """
    return text


# Convenience dictionary for easy access
CHARACTER_CONVERTERS = {
    "greek": convert_greek_characters_to_english,
    "swedish": convert_swedish_characters_to_english,
    "german": convert_german_characters_to_english,
    "french": convert_french_characters_to_english,
    "spanish": convert_spanish_characters_to_english,
    "none": no_conversion,
}


def get_character_converter(language: str = "none") -> Callable[[str], str]:
    """
    Get a character converter function by language name.

    Args:
        language: Language name ('greek', 'swedish', 'german', 'french', 'spanish', 'none')

    Returns:
        Character converter function

    Raises:
        ValueError: If language is not supported
    """
    if language not in CHARACTER_CONVERTERS:
        available = ", ".join(CHARACTER_CONVERTERS.keys())
        raise ValueError(f"Unsupported language '{language}'. Available: {available}")

    return CHARACTER_CONVERTERS[language]

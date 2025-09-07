"""
Character conversion utilities for different languages.
This module provides various character conversion functions that can be used
across multiple projects for converting characters from various languages to English equivalents.
"""

from typing import Callable, Dict


def convert_greek_characters_to_english(text: str) -> str:
    """
    Convert Greek characters to English equivalents.

    Args:
        text: Text containing Greek characters

    Returns:
        Text with Greek characters converted to English equivalents
    """
    greek_to_english_mapping: Dict[str, str] = {
        "Α": "A",
        "Β": "B",
        "Γ": "G",
        "Δ": "D",
        "Ε": "E",
        "Ζ": "Z",
        "Η": "H",
        "Θ": "TH",
        "Ι": "I",
        "Κ": "K",
        "Λ": "L",
        "Μ": "M",
        "Ν": "N",
        "Ξ": "X",
        "Ο": "O",
        "Π": "P",
        "Ρ": "R",
        "Σ": "S",
        "Τ": "T",
        "Υ": "Y",
        "Φ": "F",
        "Χ": "CH",
        "Ψ": "PS",
        "Ω": "O",
        "α": "a",
        "ά": "a",
        "β": "b",
        "γ": "g",
        "δ": "d",
        "ε": "e",
        "έ": "e",
        "ζ": "z",
        "η": "h",
        "ή": "h",
        "θ": "th",
        "ι": "i",
        "ί": "i",
        "κ": "k",
        "λ": "l",
        "μ": "m",
        "ν": "n",
        "ξ": "x",
        "ό": "o",
        "ο": "o",
        "π": "p",
        "ρ": "r",
        "σ": "s",
        "τ": "t",
        "υ": "y",
        "ύ": "y",
        "φ": "f",
        "χ": "ch",
        "ψ": "ps",
        "ω": "o",
        "ώ": "o",
        "ς": "s",  # Special case for lowercase final sigma
    }

    return "".join(greek_to_english_mapping.get(char, char) for char in text)


def convert_swedish_characters_to_english(text: str) -> str:
    """
    Convert Swedish characters to English equivalents.

    Args:
        text: Text containing Swedish characters

    Returns:
        Text with Swedish characters converted to English equivalents
    """
    swedish_to_english_mapping: Dict[str, str] = {
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
    german_to_english_mapping: Dict[str, str] = {
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
    french_to_english_mapping: Dict[str, str] = {
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
    spanish_to_english_mapping: Dict[str, str] = {
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

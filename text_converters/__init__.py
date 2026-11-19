"""
Text Converters Package

A shared package for character conversion utilities across multiple languages.
Provides functions to convert characters from various languages to English equivalents.
"""

from .character_converters import (
    CHARACTER_CONVERTERS,
    convert_french_characters_to_english,
    convert_german_characters_to_english,
    convert_greek_characters_to_english,
    convert_spanish_characters_to_english,
    convert_swedish_characters_to_english,
    get_character_converter,
    no_conversion,
)

__version__ = "0.2.0"
__author__ = "Nikos Paximadakis"

__all__ = [
    "convert_greek_characters_to_english",
    "convert_swedish_characters_to_english",
    "convert_german_characters_to_english",
    "convert_french_characters_to_english",
    "convert_spanish_characters_to_english",
    "no_conversion",
    "CHARACTER_CONVERTERS",
    "get_character_converter",
]

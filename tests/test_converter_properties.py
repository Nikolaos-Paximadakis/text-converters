"""Properties every converter must keep, checked over whole alphabets."""

import string
import unicodedata

import pytest

import text_converters
from text_converters import (
    CHARACTER_CONVERTERS,
    convert_french_characters_to_english,
    convert_german_characters_to_english,
    convert_greek_characters_to_english,
    convert_spanish_characters_to_english,
    convert_swedish_characters_to_english,
)

# Every assigned letter of the modern Greek alphabet, with tonos and diaeresis
# (U+0386 to U+03CE). A letter missing from the map would come back unchanged.
GREEK_LETTERS = "".join(
    chr(code)
    for code in range(0x0386, 0x03CF)
    if unicodedata.category(chr(code)).startswith("L")
)

# The letters each language writes, per converter.
LANGUAGE_LETTERS = {
    "swedish": (convert_swedish_characters_to_english, "åäöéÅÄÖÉ"),
    "german": (convert_german_characters_to_english, "äöüßÄÖÜ"),
    "french": (
        convert_french_characters_to_english,
        "àâçéèêëîïôùûüÿÀÂÇÉÈÊËÎÏÔÙÛÜŸ",
    ),
    "spanish": (convert_spanish_characters_to_english, "áéíóúüñÁÉÍÓÚÜÑ"),
    "greek": (convert_greek_characters_to_english, GREEK_LETTERS),
}

PRINTABLE_ASCII = string.printable


def test_greek_letter_set_is_complete():
    # 7 letters with tonos, 24 capitals, 2 capitals with diaeresis, 25 lowercase
    # (with final sigma), 7 with tonos, 2 with diaeresis, 2 with both.
    assert len(GREEK_LETTERS) == 69


@pytest.mark.parametrize("language", sorted(LANGUAGE_LETTERS))
def test_every_letter_of_the_language_becomes_ascii(language):
    convert, letters = LANGUAGE_LETTERS[language]
    for letter in letters:
        result = convert(letter)
        assert result.isascii() and result, f"{letter!r} -> {result!r}"


@pytest.mark.parametrize("language", sorted(LANGUAGE_LETTERS))
def test_capital_gives_the_capitalised_lowercase_result(language):
    convert, letters = LANGUAGE_LETTERS[language]
    for letter in letters:
        if not letter.islower() or len(letter.upper()) != 1:
            continue  # ß and ΐ/ΰ have no single-character capital
        lower, upper = convert(letter), convert(letter.upper())
        assert upper == lower.capitalize(), f"{letter!r}: {lower!r} vs {upper!r}"


@pytest.mark.parametrize("name", sorted(CHARACTER_CONVERTERS))
def test_ascii_text_is_left_unchanged(name):
    assert CHARACTER_CONVERTERS[name](PRINTABLE_ASCII) == PRINTABLE_ASCII


@pytest.mark.parametrize("language", sorted(LANGUAGE_LETTERS))
def test_converting_twice_changes_nothing(language):
    convert, letters = LANGUAGE_LETTERS[language]
    once = convert(letters)
    assert convert(once) == once


@pytest.mark.parametrize(
    "greek_text, latin",
    [
        ("Θ1", "Th1"),  # a digit after a lone capital is not a capitals word
        ("1Θ", "1Th"),
        ("ΑΘ", "ATH"),  # last letter of a capitals word
        ("ΑΘ.", "ATH."),
        ("ΘΧ", "THCH"),  # two capital digraphs side by side
        ("(Ψ)", "(Ps)"),
        ("Ου", "Ou"),
        ("ΟΥ", "OU"),
        ("όυ", "ou"),
        ("υο", "yo"),  # only ο followed by υ is a pair
        ("ουου", "ouou"),
    ],
)
def test_greek_context_rules_at_the_edges(greek_text, latin):
    assert convert_greek_characters_to_english(greek_text) == latin


def test_public_api():
    assert set(text_converters.__all__) == {
        "CHARACTER_CONVERTERS",
        "convert_french_characters_to_english",
        "convert_german_characters_to_english",
        "convert_greek_characters_to_english",
        "convert_spanish_characters_to_english",
        "convert_swedish_characters_to_english",
        "get_character_converter",
        "no_conversion",
    }
    for name in text_converters.__all__:
        assert hasattr(text_converters, name)
    assert isinstance(text_converters.__version__, str)

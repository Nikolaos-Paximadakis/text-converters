"""
Tests for character_converters module.
"""

import pytest
from text_converters.character_converters import (
    convert_greek_characters_to_english,
    convert_swedish_characters_to_english,
    convert_german_characters_to_english,
    convert_french_characters_to_english,
    convert_spanish_characters_to_english,
    no_conversion,
    get_character_converter,
    CHARACTER_CONVERTERS,
)


class TestGreekConversion:
    """Test Greek character conversion."""

    def test_basic_greek_conversion(self):
        """Test basic Greek to English conversion."""
        greek_text = "Αθήνα"
        result = convert_greek_characters_to_english(greek_text)
        assert result == "Athhna"

    def test_mixed_greek_english(self):
        """Test mixed Greek and English text."""
        mixed_text = "Hello Αθήνα World"
        result = convert_greek_characters_to_english(mixed_text)
        assert result == "Hello Athhna World"

    def test_empty_string(self):
        """Test empty string conversion."""
        result = convert_greek_characters_to_english("")
        assert result == ""

    def test_no_greek_characters(self):
        """Test text with no Greek characters."""
        english_text = "Hello World"
        result = convert_greek_characters_to_english(english_text)
        assert result == "Hello World"


class TestSwedishConversion:
    """Test Swedish character conversion."""

    def test_basic_swedish_conversion(self):
        """Test basic Swedish to English conversion."""
        swedish_text = "Göteborg"
        result = convert_swedish_characters_to_english(swedish_text)
        assert result == "Goteborg"

    def test_swedish_umlauts(self):
        """Test Swedish umlauts conversion."""
        swedish_text = "Åäö"
        result = convert_swedish_characters_to_english(swedish_text)
        assert result == "Aao"


class TestGermanConversion:
    """Test German character conversion."""

    def test_basic_german_conversion(self):
        """Test basic German to English conversion."""
        german_text = "München"
        result = convert_german_characters_to_english(german_text)
        assert result == "Muenchen"

    def test_german_eszett(self):
        """Test German eszett conversion."""
        german_text = "Straße"
        result = convert_german_characters_to_english(german_text)
        assert result == "Strasse"


class TestFrenchConversion:
    """Test French character conversion."""

    def test_basic_french_conversion(self):
        """Test basic French to English conversion."""
        french_text = "François"
        result = convert_french_characters_to_english(french_text)
        assert result == "Francois"

    def test_french_accents(self):
        """Test French accents conversion."""
        french_text = "café"
        result = convert_french_characters_to_english(french_text)
        assert result == "cafe"


class TestSpanishConversion:
    """Test Spanish character conversion."""

    def test_basic_spanish_conversion(self):
        """Test basic Spanish to English conversion."""
        spanish_text = "España"
        result = convert_spanish_characters_to_english(spanish_text)
        assert result == "Espana"

    def test_spanish_tilde(self):
        """Test Spanish tilde conversion."""
        spanish_text = "niño"
        result = convert_spanish_characters_to_english(spanish_text)
        assert result == "nino"


class TestNoConversion:
    """Test no conversion function."""

    def test_no_conversion_returns_original(self):
        """Test that no_conversion returns original text."""
        text = "Hello World 123"
        result = no_conversion(text)
        assert result == text

    def test_no_conversion_with_special_chars(self):
        """Test no_conversion with special characters."""
        text = "Hello @#$%^&*()"
        result = no_conversion(text)
        assert result == text


class TestCharacterConverter:
    """Test character converter function."""

    def test_get_greek_converter(self):
        """Test getting Greek converter."""
        converter = get_character_converter("greek")
        assert converter == convert_greek_characters_to_english

    def test_get_swedish_converter(self):
        """Test getting Swedish converter."""
        converter = get_character_converter("swedish")
        assert converter == convert_swedish_characters_to_english

    def test_get_german_converter(self):
        """Test getting German converter."""
        converter = get_character_converter("german")
        assert converter == convert_german_characters_to_english

    def test_get_french_converter(self):
        """Test getting French converter."""
        converter = get_character_converter("french")
        assert converter == convert_french_characters_to_english

    def test_get_spanish_converter(self):
        """Test getting Spanish converter."""
        converter = get_character_converter("spanish")
        assert converter == convert_spanish_characters_to_english

    def test_get_none_converter(self):
        """Test getting none converter."""
        converter = get_character_converter("none")
        assert converter == no_conversion

    def test_get_invalid_converter(self):
        """Test getting invalid converter raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported language 'invalid'"):
            get_character_converter("invalid")

    def test_converter_functionality(self):
        """Test that converter actually works."""
        converter = get_character_converter("greek")
        result = converter("Αθήνα")
        assert result == "Athhna"


class TestCharacterConvertersDict:
    """Test CHARACTER_CONVERTERS dictionary."""

    def test_character_converters_contains_all_converters(self):
        """Test that CHARACTER_CONVERTERS contains all expected converters."""
        expected_converters = [
            "none",
            "greek",
            "swedish",
            "german",
            "french",
            "spanish",
        ]
        for converter_name in expected_converters:
            assert converter_name in CHARACTER_CONVERTERS

    def test_character_converters_are_callable(self):
        """Test that all converters in CHARACTER_CONVERTERS are callable."""
        for converter_name, converter_func in CHARACTER_CONVERTERS.items():
            assert callable(converter_func), f"Converter {converter_name} is not callable"

    def test_character_converters_return_strings(self):
        """Test that all converters return strings."""
        test_text = "Test"
        for converter_name, converter_func in CHARACTER_CONVERTERS.items():
            result = converter_func(test_text)
            assert isinstance(result, str), f"Converter {converter_name} did not return a string"

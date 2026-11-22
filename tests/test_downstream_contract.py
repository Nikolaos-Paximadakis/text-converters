"""What downstream packages rely on; changing any of it is a breaking change.

sru-generator loads converters by name through ``get_character_converter`` and only
uses this package when the Greek converter gives the probe result below (an older
release that does not is ignored in favour of its own copy).
"""

from collections.abc import Callable

import pytest

import text_converters

CONVERTER_NAMES = ("none", "greek", "swedish", "german", "french", "spanish")
GREEK_PROBE = ("Θεσσαλονίκη Παπαδόπουλος", "Thessaloniki Papadopoulos")


@pytest.mark.parametrize("name", CONVERTER_NAMES)
def test_every_converter_name_resolves(name: str) -> None:
    converter: Callable[[str], str] = text_converters.get_character_converter(name)
    assert isinstance(converter("Test"), str)


def test_converter_names_are_exactly_the_documented_ones() -> None:
    assert set(text_converters.CHARACTER_CONVERTERS) == set(CONVERTER_NAMES)


def test_greek_probe_used_by_sru_generator() -> None:
    greek = text_converters.get_character_converter("greek")
    assert greek(GREEK_PROBE[0]) == GREEK_PROBE[1]


def test_unknown_name_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Unsupported language"):
        text_converters.get_character_converter("klingon")

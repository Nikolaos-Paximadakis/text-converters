"""Greek converter: η as "i", ου as "ou", Th/Ch/Ps capitalised by context."""

import pytest

from text_converters import convert_greek_characters_to_english as greek


@pytest.mark.parametrize(
    "greek_text, latin",
    [
        ("Θεσσαλονίκη", "Thessaloniki"),
        ("Χανιά", "Chania"),
        ("Ηράκλειο", "Irakleio"),
        ("Ψυχικό", "Psychiko"),
        ("Αθήνα", "Athina"),
    ],
)
def test_place_names(greek_text, latin):
    assert greek(greek_text) == latin


def test_capitals_stay_capitals():
    assert greek("ΘΕΣΣΑΛΟΝΙΚΗ") == "THESSALONIKI"
    assert greek("ΑΘΗΝΑ") == "ATHINA"
    assert greek("ΧΑΝΙΑ ΨΥΧΗ") == "CHANIA PSYCHI"
    assert greek("ΤΡΑΠΕΖΑ ΠΕΙΡΑΙΩΣ") == "TRAPEZA PEIRAIOS"


def test_digraph_at_the_end_of_a_capital_word():
    assert greek("ΚΑΛΥΨ") == "KALYPS"


def test_a_lone_capital_digraph_is_title_case():
    assert greek("Θ") == "Th"
    assert greek("Χ. Παπαδόπουλος") == "Ch. Papadopoulos"


def test_omicron_upsilon_is_ou():
    assert greek("Παπαδόπουλος") == "Papadopoulos"
    assert greek("ΟΥΡΑΝΟΥΠΟΛΗ") == "OURANOUPOLI"
    assert greek("Ούζο") == "Ouzo"
    assert greek("Υδρα κύμα") == "Ydra kyma"  # υ alone stays y


def test_eta_with_and_without_tonos():
    assert greek("ήη ΉΗ") == "ii II"


def test_accented_capitals_and_diaeresis():
    assert greek("Άλφα Ώρα") == "Alfa Ora"
    assert greek("Ά Έ Ή Ί Ό Ύ Ώ Ϊ Ϋ ϊ ϋ ΐ ΰ") == "A E I I O Y O I Y i y i y"


def test_text_that_is_not_greek_is_unchanged():
    assert greek("Åsa Öberg 123 ABB") == "Åsa Öberg 123 ABB"


def test_existing_examples_still_hold():
    assert greek("Ελλάδα") == "Ellada"
    assert greek("Τράπεζα Πειραιώς") == "Trapeza Peiraios"

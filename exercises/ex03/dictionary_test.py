"""Dictionary Assignent Unit Tests"""

__author__ = "730747262"


from dictionary import invert
from dictionary import count
from dictionary import favorite_color
from dictionary import bin_len


def test_invert() -> None:
    """First Unit Test for "Invert", Use Case"""
    assert invert({"D": "Daniel", "G": "Greg", "T": "Tri"}) == {
        "Daniel": "D",
        "Greg": "G",
        "Tri": "T",
    }


def test_invert_1() -> None:
    """Second unit test for "Invert", Use Case"""
    assert invert({"Dog": "Cat", "Start": "Stop", "Slow": "Fast"}) == {
        "Cat": "Dog",
        "Stop": "Start",
        "Fast": "Slow",
    }


def test_invert_2() -> None:
    """Third unit test for "Invert", edge case"""
    assert invert({}) == {}


def test_count() -> None:
    """First unit test for "Count", use case"""
    assert count(["dog", "dog", "four", "small", "pugnant", "four", "four"]) == {
        "dog": 2,
        "four": 3,
        "small": 1,
        "pugnant": 1,
    }


def test_count_2() -> None:
    """Seocnd unit tets for "Count", use case"""
    assert count(["a", "a", "a", "b", "c", "c", "d", "d", "d", "d", "d", "e"]) == {
        "a": 3,
        "b": 1,
        "c": 2,
        "d": 5,
        "e": 1,
    }


def test_count_3() -> None:
    """Third unit test for "Count", edge case"""
    assert count(["a"]) == {"a": 1}


def test_favorite_color() -> None:
    """First unit test for "Favorite Color", unit case"""
    assert (
        favorite_color(
            {
                "Eun": "Blue",
                "Greg": "Blue",
                "Miriam": "Pink",
                "Seoyun": "Blue",
                "Aiah": "Blue",
                "Tina": "Purple",
                "Chandi": "Black",
            }
        )
        == "Blue"
    )


def test_favorite_color_2() -> None:
    """Second unit test for "Favorite Color", unit case"""
    assert (
        favorite_color(
            {
                "Mom": "Purple",
                "Dad": "Red",
                "Bryan": "Black",
                "Daniel": "Purple",
                "Mary": "Pink",
                "Andrew": "Blue",
                "Thomas": "Purple",
                "Lauren": "Pink",
            }
        )
        == "Purple"
    )


def test_favorite_color_3() -> None:
    """Third unit test for "Favorite Color", edge case"""
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    """First unit test for "Bin Len", use case"""
    assert bin_len(["dog", "dog", "four", "small", "pugnant", "four", "four"]) == {
        3: {"dog", "dog"},
        4: {"four", "four", "four"},
        5: {"small"},
        7: {"pugnant"},
    }


def test_bin_len_2() -> None:
    """Second unit test for "Bin Len", use case"""
    assert bin_len(["ate", "pier", "nicer", "scrumptious"]) == {
        3: {"ate"},
        4: {"pier"},
        5: {"nicer"},
        11: {"scrumptious"},
    }


def test_bin_len_3() -> None:
    """Third unit test for "Bin Len", edge case"""
    assert bin_len([]) == {}

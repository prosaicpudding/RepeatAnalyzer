import pytest

from RepeatAnalyzer.RA_DataStructures import Location


@pytest.mark.parametrize("input_string,expected", [
        ("",""),
        ("U. S. A., Conneticut, Fake Place St.","U. S. A., Conneticut, Fake Place St."),
        ("123.12345, 67.12345", "")
    ])
def test_location_str(input_string, expected):
    test_location = Location(input_string)

    assert str(test_location) == expected

@pytest.mark.parametrize("input_string,expected", [
        ("","(None, None)"),
        ("U. S. A., Conneticut, Fake Place St.","U. S. A., Conneticut, Fake Place St., (None, None)"),
        ("123.12345, 67.12345", "(123.12345, 67.12345)")
    ])
def test_location_repr(input_string, expected):
    test_location = Location(input_string)

    assert repr(test_location) == expected

@pytest.mark.parametrize("input_string,params,expected", [
        ("",{},""),
        ("U. S. A., Conneticut, Fake Place St.", {"country_first":True, "coords":True},"U. S. A., Conneticut, Fake Place St., (None, None)"),
        ("U. S. A., Conneticut, Fake Place St.", {"country_first":False, "coords":False},"Fake Place St., Conneticut, U. S. A."),
        ("123.12345, 67.12345",{"country_first":True, "coords":True} , "(123.12345, 67.12345)")
    ])
def test_location_getString(input_string, params,expected):
    test_location = Location(input_string)

    assert test_location.getString(**params) == expected

@pytest.mark.parametrize("input_string,expected", [
        ("",0),
        ("U. S. A., Conneticut, Fake Place St.", 3),
        ("South Africa", 1),
        ("South Africa, Western Cape", 2),
        ("South Africa, Western Cape,", 2),
        ("South Africa, Western Cape, Cape Town", 3),
        ("123.12345, 67.12345", 0)
    ])
def test_location_len(input_string, expected):
    test_location = Location(input_string)

    assert len(test_location) == expected

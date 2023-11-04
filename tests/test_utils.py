from time import sleep

import pytest

from RepeatAnalyzer.utils import (get_coords_from_location_name,
                                  get_location_name_from_coords)


@pytest.mark.parametrize("location_name,expected", [
    ("", (None, None)),
    ("Fake Place Street, 123", (None, None)),
    ("Albion, Washington", (46.7909974, -117.250452)),
    ("Minnesota", (45.9896587, -94.6113288)),
    ("Minnesota, USA", (45.9896587, -94.6113288)),
    ("Cape town, South Africa", (-33.928992, 18.417396)),
    ("Florida, USA", (27.7567667, -81.4639835)),
    ("U.S.A., Idaho, St. Maries.", (47.3143542, -116.562667)),
    ("USA, Idaho, St Maries", (47.3143542, -116.562667)),
    ("Baker County, Oregon, United States", (44.7259637, -117.6204818)),
    ("U. S. A., Kansas", (38.27312, -98.5821872)),
    ({"country":"United States", "state":"Washington", "subdivision": ""},(47.2868352, -120.212613)),
    ({"country": "South Africa", "state": "KwaZulu-Natal", "subdivision": ""}, (-28.503833, 30.8875009)),
    ({"city": "platte", "state": "South Dakota", "country": "USA"}, (43.38694, -98.84453)),
    ("Platte, South Dakota, United States", (43.38694, -98.84453)),
    ("Batangas, Calabarzon, Philippines", (13.9146826, 121.0867566)),
    ("Philippines, Batangas", (13.9146826, 121.0867566)),
    ("Philippines, Central Visayas, Negros Oriental", (9.75, 123.0)),
    ("Philippines, Western Visayas, Negros Occidental", (10.416667, 123.0)),
    ("Antioquia, Columbia", (7.0000085, -75.5000086)),
    ({"state":"Antioquia", "country":"Columbia"}, (7.0000085, -75.5000086)),

])
def test_get_coords_from_location_name(location_name, expected):
    sleep(0.3)

    assert get_coords_from_location_name(location_name) == expected

@pytest.mark.parametrize("latitude,longitude,expected", [
    (46.7909974, -117.250452, {"city": "Albion", "province": "Washington", "country": "United States"}),
    (45.9896587, -94.6113288, {"city": "Morrison County", "country": "United States", "province": "Minnesota"}),
    (45.9896597, -94.6113288, {"city": "Morrison County", "country": "United States", "province": "Minnesota"}),
    (-33.928992, 18.417396, {"city": "Cape Town", "country": "South Africa", "province": "Western Cape"}),
    (32.937094, 35.083828, {"city": "Acre", "province": "North District", "country": "Israel"}), # Ensure locations code in English
])
def test_get_location_name_from_coords(latitude, longitude, expected):
    sleep(0.3)

    location = get_location_name_from_coords(latitude=latitude, longitude=longitude)

    assert location == expected

import logging
import os
import re
import sys
from logging.handlers import RotatingFileHandler
from typing import Union

from geopy.geocoders import Nominatim

from RepeatAnalyzer.constants import problem_place_names, version


def get_working_directory() -> str:
    """
    Get the working directory of the script/exe.
    This allows us to keep data files in the same directory as the script/exe.

    Returns:
        str: The working directory of the script/file.
    """
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle
        return os.path.dirname(sys.executable)
    else:
        # Running as a script
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set logger to the lowest level of logging

# File handler for logging DEBUG and above to file
os.makedirs(os.path.join(get_working_directory(),"logs"), exist_ok=True)
fh = RotatingFileHandler(
        os.path.join(get_working_directory(),"logs", "repeatanalyzer.log"),
        mode="w",
        encoding="UTF-8",
        maxBytes=2000000,
        backupCount=10
    )
fh.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s: %(levelname)8s: %(message)s')
fh.setFormatter(log_formatter)
logger.addHandler(fh)

# Console handler for logging ERROR and above to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
ch.setFormatter(console_formatter)
logger.addHandler(ch)


# This function takes a given IDlist and returns the earliest unused ID,
# also adding it to the list
def newID(IDlist: set[int]) -> int:
    nextID = 0
    for id in sorted(IDlist):
        if id == nextID:
            nextID += 1
        else:
            IDlist.add(nextID)
            return nextID
    IDlist.add(nextID)
    return nextID


# given a single entity name and a list of entities,
# returns the id of the entity in the list
def findID(name: str, entity_list: list[str]) -> Union[int, None]:
    name = name.strip()
    for item in entity_list:
        for next in item.name:
            if next == name:
                return item.ID
    return None


def sanitize(string:str) -> str:
	"""Remove whitespace, punctuation and numbers from the string. Convert it to lower case

	Args:
		string (str): the string to be sanitized

	Returns:
		str : the sanitized string
	"""
	string = re.sub(r"[^\w]", "", string)
	string = re.sub(r"[\d_]", "", string)
	string = string.lower()
	return string


def remove_punctuation_except_comma(string:str) -> str:
    """ Remove all punctuation from a string except for commas"""
    return re.sub(r'[^\w\s,-]', '', string)


def replace_words(string:str, replacements:dict[str,str]=problem_place_names) -> str:
    """ Replace words in a string with other words, according to a dictionary of replacements"""
    for old_word, new_word in replacements.items():
        string = string.replace(old_word, new_word)
    return string


def get_coords_from_location_name(location_name:Union[str,dict], verbose:bool=True) -> tuple[float, float]:
    """ Get the coordinates of a location from its name

    Args:
        location_name (Union[str,dict]): the name of the location to be searched for OR a dictionary containing the location name
            ex. "USA, Maine" or {"country":"USA", "province":"Maine"}

    Returns:
        tuple[float, float]: the latitude and longitude of the location
    """
    if isinstance(location_name, str):
        location_name = remove_punctuation_except_comma(replace_words(location_name))
    else:
        for key, value in location_name.items():
            location_name[key] = remove_punctuation_except_comma(replace_words(value))

    geolocator = Nominatim(user_agent=f"RepeatAnalyzer_{version}", timeout=12)
    location = geolocator.geocode(location_name, language='en', exactly_one=True)

    if location == None:
        logger.info(f"Failed to find coordinates for {location_name}")
        return None, None

    return (location.latitude, location.longitude)

def get_location_name_from_coords(latitude:float, longitude:float, verbose:bool=False) -> dict[str]:
    """ Find a location name from its coordinates

    Args:
        latitude (float): The latitude
        longitude (float): The longitude

    Returns:
        dict[str]: A dictionary containing the location name
            ex. {"country":"USA", "province":"Maine"}
    """
    geolocator = Nominatim(user_agent=f"RepeatAnalyzer_{version}", timeout=12)
    location = geolocator.reverse((latitude, longitude), exactly_one=True, language='en')
    if location == None:
        return None

    # Accessing the raw JSON data
    address = location.raw['address']
    if verbose:
        logger.info(f"Full result: {address}")

    # Constructing our standardized dictionary
    address_dict = {
        "city": address.get('city',
                                address.get('town',
                                            address.get('village',
                                                        address.get('hamlet',
                                                                    address.get('county', ''))))),
        "province": address.get('state', address.get('province', address.get('region',''))),
        "country": address.get('country', '')
    }
    return address_dict

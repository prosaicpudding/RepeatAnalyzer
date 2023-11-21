#!/usr/bin/env python
# coding: utf-8
# 	 Copyright 2015 Helen Catanese

#    This file is part of RepeatAnalyzer.

#    RepeatAnalyzer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    RepeatAnalyzer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with RepeatAnalyzer.  If not, see <http://www.gnu.org/licenses/>.


import logging
import tkinter.messagebox
# from Tkinter import *
from tkinter.scrolledtext import *

from RepeatAnalyzer.utils import (findID, get_coords_from_location_name,
                                  get_location_name_from_coords, newID,
                                  sanitize)


class Repeat:
    def __init__(self, name, sequence, ID):  # name=list, repeats=string
        self.ID = ID
        self.name = name
        self.sequence = sequence  # the repeat
        self.subsetOf = []


class Strain:
    def __init__(
        self, name, repeats, ID, locationstring, accessionCode=[]
    ):  # name=list, repeats=list of IDs
        self.autoname = []
        nparts = name[0].strip().split(",")
        if len(nparts) == 2 and len(nparts[0].strip()) == 4:
            name = [""]
            self.autoname.append((nparts[0].strip(), nparts[1].strip(), locationstring))
        self.ID = ID
        self.name = name
        self.sequence = repeats
        self.location = [Location(locationstring)]
        self.subsetOf = []
        self.accessionCode = accessionCode


class Species:
    def __init__(self, name):
        self.name = name  # the species name
        self.repeats = []  # the list of repeats
        self.strains = []  # the list of strains
        self.usedRepeatIDs = set([])
        self.usedStrainIDs = set([])
        self.paperList = []
        self.dummyLocations = set([])

    ##This function takes the info for a new repeat and adds it,
    ##or if it has a new sequence with existing name asks the user if they want to replace it.
    def addRepeat(self, name, sequence):
        from tkinter import Tk

        found = findID(name, self.repeats)
        root = Tk()
        root.withdraw()

        for repeat in self.repeats:
            if repeat.ID == found and repeat.sequence != sequence:
                if tkinter.messagebox.askyesno(
                    "Conflict",
                    "The repeat "
                    + name
                    + " already exists with sequence "
                    + repeat.sequence
                    + " Would you like to replace it with the sequence "
                    + sequence,
                ):
                    repeat.sequence = sequence  # update sequence
                    return 0
                else:
                    if tkinter.messagebox.askyesno(
                        "Conflict",
                        "Would you like to save " + name + " as a new repeat?",
                    ):
                        tkinter.messagebox.showinfo(
                            "Instructions",
                            "You will need to change the name of "
                            + name
                            + " in the input file."
                            + "\n"
                            + "Be sure to also update the names of any strains referring to this same sequence"
                            + sequence
                            + "\n"
                            + "Ex. You could call this repeat "
                            + name
                            + "-1 or "
                            + name
                            + "(2)"
                            + "\n"
                            + "Once you have updated the file, be sure to run this function again to read the rest of the input",
                        )
                        return 1
            if repeat.sequence == sequence and (name not in repeat.name):
                repeat.name.append(name)  # add new names
                return 0

        if found == None:
            self.repeats.append(Repeat([name], sequence, newID(self.usedRepeatIDs)))

    def addStrain(
        self, name, repeats, locationstring, accessionCode=[]
    ):  # name=list, repeats=string of repeat names
        repeatIDs = parserepeats(repeats, self)
        if repeatIDs == []:
            return
        nparts = name[0].strip().split(",")
        # print len(nparts), len(nparts[0])

        # check if the sequence exists
        found = identifystrain(repeatIDs, self)
        if found != None:
            for strain in self.strains:
                if strain.ID == found:
                    # if autogen naming, add name info
                    if len(nparts) == 2 and len(nparts[0].strip()) == 4:
                        name = [""]
                        if hasattr(strain, "autoname") == False:
                            strain.autoname = []
                        strain.autoname.append(
                            (nparts[0].strip(), nparts[1].strip(), locationstring)
                        )

                    # add name to found names
                    strain.name = list(set(name) | set(strain.name))
                    # add acc code to list
                    strain.accessionCode = list(
                        set(accessionCode) | set(strain.accessionCode)
                    )
                    while "" in strain.name and len(strain.name) > 1:
                        strain.name.remove("")

                    # add location to found locations
                    l = Location(locationstring)
                    locfound = False
                    for loc in strain.location:
                        if l == loc:
                            locfound = True
                            break
                    if locfound == False:
                        strain.location.append(l)
                    return
        else:
            newstrain = Strain(
                name,
                repeatIDs,
                newID(self.usedStrainIDs),
                locationstring,
                accessionCode,
            )
            if len(newstrain.sequence) > 0:
                self.strains.append(newstrain)
        return

    def addPaper(self, newpaper):
        if newpaper.type == "u":
            for paper in self.paperList:
                if (
                    newpaper.authors == paper.authors
                    and newpaper.year == paper.year
                    and paper.title == newpaper.title
                ):
                    return paper
        else:
            for paper in self.paperList:
                if paper.type != "u" and newpaper.PMID == paper.PMID:
                    return paper

        self.paperList.append(newpaper)
        return newpaper

    def addlocationdummies(self, location):
        loc = location.split(",")
        if len(loc) > 1:
            # add level 1 dummy
            self.dummyLocations.add(Location(loc[0]))
        if len(loc) == 3:
            # add level 2 dummy
            self.dummyLocations.add(Location(loc[0] + "," + loc[1]))


class Paper:
    def __init__(self, lines, type="p"):
        if len(lines) != 3:
            print("Error in input, citation formatted incorrectly")
            return

        self.line1 = lines[0]
        self.line2 = lines[1]
        self.line3 = lines[2]
        self.authors = lines[1].strip().split(",.")
        for a in self.authors:
            a = a.strip()
        [a for a in self.authors if a != ""]
        self.repeats = set([])
        self.strains = set([])

        if lines[0] == "Unpublished:":
            self.title = "Unpublished"
            self.type = "u"
            self.year = lines[1].strip()
        else:
            self.type = type
            l3 = lines[2].split(".")
            self.year = l3[1].strip().split(" ")[0]
            self.journal = l3[0]
            # print l3
            # print l3[-1].strip().split(" ")
            self.PMID = l3[-1].strip().split(" ")[-1]
            self.title = lines[0].strip()

        return

    def addRepeat(self, ID):
        self.repeats.add(ID)
        return

    def addStrain(self, ID):
        self.strains.add(ID)
        return

    def hasRepeat(self, ID):
        return ID in self.repeats

    def hasStrain(self, ID):
        return ID in self.strains


class Location:
    def __init__(self, string):
        string = string.strip()
        list = string.split(",")
        self.locationstring = string
        self.country = ""  # the country
        self.province = ""
        self.city = ""
        self.pcode = ""
        self.ccode = ""
        self.latitude = None
        self.longitude = None
        self.stable = False
        if string == "":
            return
        try:
            self.latitude = float(list[0])
            if len(list) < 2:
                print("Error, invalid location,", string, "missing longitude")
                return
            self.longitude = float(list[1])
        except ValueError:
            self.country = list[0].strip()  # the country
            if len(list) > 1:
                self.province = list[1].strip()  # the province or region
            if len(list) > 2:
                self.city = list[2].strip()  # the city, town or county

    def __eq__(self, l) -> bool:
        if l == None:
            return False
        if len(l) == 0:
            return self.latitude == l.latitude and self.longitude == l.longitude
        return (
            sanitize(self.country) == sanitize(l.country)
            and sanitize(self.province) == sanitize(l.province)
            and sanitize(self.city) == sanitize(l.city)
        )

    def getList(self) -> list[str]:
        if len(self) == 1:
            return [self.country]
        if len(self) == 2:
            return [self.country, self.province]

        return [self.country, self.province, self.city]

    def getString(self, country_first=True, coords=False) -> str:
        # Initialize an empty list to hold the location parts.
        location_parts = []

        # Add the location parts based on the 'length' attribute.
        if len(self) >= 1:
            location_parts.append(self.country)
        if len(self) >= 2:
            location_parts.append(self.province)
        if len(self) == 3:
            location_parts.append(self.city)

        # Reverse the order if country should not be first.
        if not country_first:
            location_parts.reverse()

        # Add the coordinates if requested.
        if coords:
            location_parts.append(f"({self.latitude}, {self.longitude})")

        # Join the location parts into a single string.
        location_str = ', '.join(location_parts)

        return location_str

    def getDict(self) -> dict:
        return{"country": self.country, "province": self.province, "city": self.city}

    def __hash__(self) -> int:
        return hash(self.getString())

    def __str__(self) -> str:
        return self.getString()

    def __repr__(self) -> str:
        return f"{self.getString(coords=True)}"

    def __len__(self) -> int:
        length = 0
        if self.country != "":
            length += 1
        if self.province != "":
            length +=1
        if self.city != "":
            length += 1
        return length

    def code_coords(self) -> None:
        logging.info(f"Coding coords for {self.__repr__()}...")
        levels = 3
        if self.latitude is None or self.longitude is None:
            levels = len(self) # Make sure we know if
            self.latitude, self.longitude = get_coords_from_location_name(self.getString(country_first=False))

        location_dict = get_location_name_from_coords(self.latitude, self.longitude)
        logging.info(f"Got {location_dict}")
        self.country = location_dict["country"]
        if levels >= 2:
            self.province = location_dict["province"]
        if levels >= 3:
            self.city = location_dict["city"]

        logging.info(f"Coded as {self.__repr__()}")

# takes a string of whitespace separated repeats and returns a list of repeat ids
def parserepeats(string, species):  # returns an array of IDs
    names = string.split()
    result = []
    for name in names:
        id = findID(name, species.repeats)
        if id == None:
            print(
                "Warning: '" + name + "' is not a repeat for",
                species.name,
                "check that it is defined in the input file.",
            )
            return []
        else:
            result.append(id)
    return result


# finds any strains in a protein list of repeats passed by ID
def identifystrain(repeats, species):
    for strain in species.strains:
        if strain.sequence == repeats:
            return strain.ID
    return None

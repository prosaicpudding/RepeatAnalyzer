# RepeatAnalyzer Quickstart Guide

## Overview

The purpose of this guide is to allow you to set up and begin using the RepeatAnalyzer software package on a new computer, with either Windows, Mac OS X or Linux operating systems. This process involves installing free software from a third party source and thus requires an internet connection. A brief description of how to use the software follows, however this is not meant to be a complete source on use cases. For questions related to problems with installation or usage of this software, contact the dev team at <https://github.com/prosaicpudding/RepeatAnalyzer/discussions>

## Download

Source code is available at: <https://github.com/prosaicpudding/RepeatAnalyzer>. You can download the sourcecoe as a zip file by clicking the green "code" button and selecting "Download Zip". Alternatively, if you are familiar with git, you can clone the repository using:

`git clone git@github.com:prosaicpudding/RepeatAnalyzer.git`

For windows users, an executable file is available [here](https://github.com/prosaicpudding/RepeatAnalyzer/releases) If you are using the executable, you can skip the installation steps below. Note that we currently don't have a budget to sign the executable file, so you will need to ignore the windows defender security warning.

## Installation
Assuming for one reason or another you are downloading the program and running it from source code, ensure you have an internet connection before you begin. These instructions assume you are familiar with your systems's command terminal.

1. Go to <https://www.python.org/downloads/>. Follow installation instructions there. Be sure to install a version that is at least 3.10.x
2. Next, we will install dependencies.
   - If you are on Mac OS, or Linux, you will likely need to install the latest versions of geos and proj using either brew (Mac OS) or apt (Linux).
   - For all operating systems, you will need to install poetry. In your system's command prompt run `python -m pip install poetry` If you get a warning that this is not a recognized command, you will need to either add your python installation to the system's PATH environment variable or (and this may be easier) use the full path to your python executable. For example, on a windows system, you might use `C:\Users\your.username\AppData\Local\Programs\Python\Python310\python.exe -m pip install poetry`
   - With poetry and system depenceindies installed, you acan use poetry to handle install the remaining python dependencies for RepeatAnalyzer. Run `poetry install` in the main source directory (where the pyproject.toml file is).
3. You can now start RepeatAnalyzer by running `poetry run python main.py` in the main source directory. Note that you should leave the MapData and all other included files in that directory, as they are required by main.py to run. With this, you are technically done. YOu can go on and use the program. But I suggest completing step 4 to save yourself some time in the future.
4. To make starting the program easier, you can create a shortcut that immediately opens repeatanalyzer in a new terminal window. To do this:
   - Create a shortcut to the command prompt application.
   - Open the properties of that shortcut (on windows, right click)
   - Change Target to `existing\path\cmd.exe /k poetry run python main.py`
   - Set the start in directory to the path of your source directory (some thing like `C:\Users\your.username\Documents\RepeatAnalyzer`)

## First time setup

When the program is run for the first time, it will warn you that the RepeatAnalyzer.dat file is missing, and ask if you wish to continue. This is normal behavior. To setup the program with the default _A. marginale_ data included with the source code, just enter ‘y’ and then 'Anaplasma marginale' as the species name (or any other species you wish to load first).  See 'Using the Main Functions' subsection 5 for details on loading in the data for the first time.

## Basics

RepeatAnalyzer uses a primarily command line interface, which means that interacting with the main menu of the program will usually involve reading options from the screen and typing in your selection. The main menu includes 11 options (currently) which can be selected by entering the corresponding number for that option. Once an option has been selected, RepeatAnalyzer may open additional dialogs, or present other command line options.

At any given time, RepeatAnalyzer will be set to work on a single species (_Anaplama marginale_, _Anaplasma centrale_, etc). Be sure that the program is set to the intended species when you are adding or searching data, as it will only access the repeats and strains stored for that particular species. If the species you wish to work with does not appear as on option in command 2 (change current species), you may add it with command 2, sub-option 0. Be sure to check the current species each time you open the program (if you are working with data for more than one species).

## Adding Data

### With existing data

If the RepeatAnalyzer.dat file is in the same folder as RepeatAnalyzer.py when it is executed, the stored data will be loaded. Upon opening the program you will see the main menu, showing the current species, and the number of strains and repeats stored respectively. If this is the correct species, continue as usual, otherwise, be sure to change the current species before moving on.

### Without existing data

If the RepeatAnalyzer.dat file is not in the same folder as the RepeatAnalyzer.py file when it is run, the program will first confirm that the RepeatAnalyzer.dat file is missing and ask if you wish to continue. If you enter 'y' (for yes) it will ask what species you would like to work with. At this point you will be prompted to enter the name (Genus species) of the species you will be adding data for. After you have done this the main menu of the program will appear, with the species name you entered and 0 strains, 0 repeats.

### In either case...

At the main menu, select command 5 and enter the name of the input file. AmarginaleData.txt comes packaged with the source code. If you wish to use another input file, make sure it follows the formatting outlined in the Sample File Formatting Section below. The program will then read this file into its internal storage. If there is an issue reading, the program will try to give the line number where the issue occurred in the file, but the error may actually be on the line before or after the one given, so check that whole area and correct any formatting mistakes until it reads in with no errors. Once reading is complete, you will be prompted on whether you would like to update the geocoding for your data. If you have an internet connection, select ‘y’, as mapping and regional analysis functionalities will be disabled until this is completed. If you select ‘n’ now, geocoding can be updated later via command 11.

Keep in mind that any strains or repeats with the same sequence will be stored as a single repeat or strain with multiple names, so if the number of repeats is lower than you were expecting after adding a file, this is likely the reason. Check the data summary (command 10) for details on where this occurred.

Note that within the included _Anaplasma marginale_ data file, the repeat ‘tc63_3_s06’ is present with no given sequence. This is not a mistake, as it was included in a publication with no sequence provided and no valid reference. It will not cause any problems in the program, only an error message when inputting the file; genotypes including it will be ignored. Keep in mind that this is the 235th repeat, as referenced in the main paper.

### Sample Input File Format

Paper:
    [citation line 1: title]
        [citation line 2:autors]
        [citation line 3: other info]
    Repeats:
        [name] : [sequence]
        {repeat for each repeat}
    Strains:
        [name (optional, but the colon is not) OR year , animalID (if using auto-naming)] : [space separated list of repeat names] : [location in the form country,province,county or country province or country]
        {repeat this for each strain. if you have one strain at multiple locations it will need to be listed twice, but rest assured it will only be counted once}
    {Repeat this pattern for each published paper}
Unpublished:
    [author name(s), this should look like 2 of paper citation]
        [year of findings]
        Repeats:       {this should be exactly the same as the repeats section for a paper}    Strains:       {likewise, this is the same as the strains section for a paper}
        {Repeat this pattern for each unpublished source}

## Using the Main Functions

Each of the following subsections outlines the capabilities of one of the 11 main menu functions which
RepeatAnalyzer performs. Each section includes details on any input required for the function, and any
output it generates. A user can access the function by entering the associated number at the main menu.

### 1. Identify repeats

__Input:__ One full or partial gene sequence either in DNA or protein form OR multiple gene sequences in FASTA format.

__Output:__ The names of the maximal set of repeats in each sample with genotype name and publication details if any.

![An example ilustrating repeat identification](Documentation\RA_fig1.png "An example ilustrating repeat identification")

*__Figure 1__ Shows the repeat/genotype identification interface. Once a sequence or sequences have been entered into the identification window (bottom left) and the correct input type is chosen (DNA or Protein), the match window will appear with which (known) repeats occur in the sequence and all relevant information on the genotype (if it has been reported previously). All windows can be resized and/or have their contents copied as needed.*

### 2. Change current species

__Input:__ The number of the species (as listed on-screen) OR 0 followed by name of the new species.

__Output:__ The main menu header will change as appropriate.

![An example ilustrating species change](Documentation\RA_fig2.png "An example ilustrating species change")

*__Figure 2__ Shows the interface to change species or add a new species. Specifically, showing the series of commands used to add a new species to RepeatAnalyzer. The first command opens the species change menu. The second selects add a species. Finally, the third accepts the name of the species from the user. Before the species is added, RepeatAnalyzer will also ask the user to enter the command 'y' to confirm that the new name is correct.*

### 3. Search Data

__Input:__ Select entity type by number, repeat, strain or location. Check boxes as desired.

- _Repeat:_ repeat name or sequence OR multiple of repeat names or sequences in FASTA format
- _Strain:_ genotype name or sequence (by repeat names) OR multiple genotype names or sequences in FASTA format
- _Location:_ location name from dropdown

__Output:__ A summary of information for the entity or entities selected. See Figures 3, 4 and 5 for illustrations of each of the three search types.

![An example ilustrating search by repeat](Documentation\RA_fig3.png "An example ilustrating search by repeat")

*__Figure 3__ Shows the search by repeat interface. Once one or more repeat names or sequences (in FASTA format) is entered along with a maximum edit distance (default zero), the search result window appears with the relevant details for that repeat. The windows are scrollable and can be copied.

![An example ilustrating search by location](Documentation\RA_fig4.png "An example ilustrating search by location")

*__Figure 4__ Shows the search by location interface. Similar to Figure 3, search by location shows all relevant information for a given location, selected from the alphabetized list in the search window. Locations can be as broad as a country, or as narrow as a county, and broader location will include results from all narrower locations as well. (i.e. the result for Brazil includes results for any Brazilian province or county with data.) If a location does not appear on the list, then there are no genotype reports in that location.

![An example ilustrating search by strain](Documentation\RA_fig5.png "An example ilustrating search by strain")

*__Figure 5__ Shows the search by strain interface. It can accept either a single strain name or sequence, or multiple in FASTA. For each input it returns the edit distances for all repeats in the strain, all locations it has been reported, and the associated publications.

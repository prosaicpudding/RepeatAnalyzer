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

# RepeatAnalyzer

> **_NOTE:_** This is a new home for the RepeatAnalyzer project found at: https://bitbucket.org/repeatgroup/repeatanalyzer/src/master/

RepeatAnalyzer is a tool for tracking, managing, analyzing and cataloguing short-sequence repeats and genotypes. It was originally built with model species _Anaplasma marginale_ in mind, but has since been used fro _Anaplasma centrale_ and tested with _Streptococcus pneumoniea_.

## User Setup

Please refer to the [user quickstart guide](https://github.com/prosaicpudding/RepeatAnalyzer/blob/main/UserGuide.md)

## Dev Setup

Requires:
   Python 3.10+
   poetry
   Windows or Mac OS
    (project may work partially in Linux but HAS NOT been tested. Development/testing in Mac OS is limited)
   Depending on your MacOs version, you may need to install additional dependencies for certain python libraries.
    see "Install Macos Dependencies" in .github/workflows/build.yml in this project for more details.

Requirements for this project are managed with poetry. That means first time setup should entail only the follwing, assuming your python installation is on the system path.
If it is not, you can replace 'python' in the first command below with your desired system python version. Once this is done, you can always run code for this project with
poetry run python. A managed virtual environment will be created on your system by poetry. For more information, use `poetry --help`

``` bash
    python -m pip install poetry
    poetry install
    poetry run python main.py
    poetry run pre-commit install  # this will activate the hooks in .pre-commit-config.yml
```

### pre-commit

This repository uses pre-commit to automate certain linting and style checks required by the project. For more information, read https://github.com/pre-commit/pre-commit-hooks

### Documenting changes

Please include any changes you would like to have merged to the main branch to CHANGELOG.md

## Notes

The most up to date version of RepeatAnalyzer.dat that I have been using in testing is also there.
It currently only has data for A. marginale and is not complete.

Additionally, some locations are stored incorrectly. For instance, in South Africa, "freestate" will not
return any results because the data is stored to "northeastern freestate". There are analogous problems
for several areas.

The MapData folder holds shapefiles of the borders used in mapping, collected from naturalearthdata.com

For areas with more than 15 or so repeats on a single point, pie charts will become blurred.

Legends may also run off the map if they contain over 20 or so entries.

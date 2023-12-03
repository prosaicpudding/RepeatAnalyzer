from setuptools import setup

APP = ['main.py', "RepeatAnalyzer"]
DATA_FILES = [('MapData', ['MapData'])]
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

import os

from setuptools import setup

from packaging_utils import extract_version_from_pyproject_toml

version = extract_version_from_pyproject_toml()

APP = ['main.py']
DATA_FILES = [
        ('MapData', ['MapData']),
        #(mpl_toolkits_path, [os.path.join("lib","python3.10","mpl_toolkits")])
    ]
OPTIONS = {
    'argv_emulation': True,
    #'zipfile': None,
    'maybe-packages': ['mpl_toolkits.basemap'],
}

setup(
    name= f"RepeatAnalyzer_v{version}",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

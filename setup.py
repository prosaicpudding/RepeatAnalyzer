from setuptools import setup

from packaging_utils import extract_version_from_pyproject_toml

version = extract_version_from_pyproject_toml()

APP = ['main.py']
DATA_FILES = [
        ('MapData', ['MapData']),
        ("RepeatAnalyzer", ["RepeatAnalyzer"]),
    ]
OPTIONS = {
    'argv_emulation': True,
}

setup(
    name= f"RepeatAnalyzer_V{version}",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

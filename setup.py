from setuptools import setup

from packaging_utils import extract_version_from_pyproject_toml

version = extract_version_from_pyproject_toml()

APP = ['main.py', "RepeatAnalyzer"]
DATA_FILES = [('MapData', ['MapData'])]
OPTIONS = {
    'argv_emulation': True,
    'py2app': {
        'APP_NAME': f'RepeatAnalyzer_V{version}',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

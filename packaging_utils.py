import os
import platform
import sys

import toml

# Get the path to the currently running Python executable
python_executable = sys.executable

def extract_version_from_pyproject_toml(file_path='pyproject.toml'):
    try:
        with open(file_path, 'r') as toml_file:
            toml_content = toml.load(toml_file)
            version = toml_content['tool']['poetry']['version']
            return version
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except KeyError:
        print(f"Error: Unable to find version in {file_path}. Make sure the file structure is correct.")
        return None

# Get the venv directory
python_executable_dir = os.path.dirname(os.path.dirname(python_executable))

if platform.system().lower() == 'windows':
    lib = "Lib"
else:
    lib = "lib/python3.10"

mpl_toolkits_path = os.path.join(python_executable_dir, lib, "site-packages", "mpl_toolkits", "basemap_data", "*")
print(f"Looking for additional requirements in: {mpl_toolkits_path}")

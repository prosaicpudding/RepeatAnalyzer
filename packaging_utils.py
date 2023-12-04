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

# print python_executable_dir contents recursively
print(f"Contents of {python_executable_dir}/{lib}:")
for root, dirs, files in os.walk(f"{python_executable_dir}/{lib}"):
    for file in files:
        print(os.path.join(root, file))

mpl_toolkits_path = os.path.join(python_executable_dir, lib, "site-packages", "mpl_toolkits")
print(f"Looking for additional requirements in: {mpl_toolkits_path}")

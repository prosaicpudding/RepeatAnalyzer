import toml


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

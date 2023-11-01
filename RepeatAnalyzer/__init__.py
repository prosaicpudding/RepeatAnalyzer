import toml

try:
    with open('../pyproject.toml', 'r') as f:
        poetry_config = toml.load(f)['tool']['poetry']
    __version__ = poetry_config['version']
except:
    __version__ = "dev"

# -*- mode: python ; coding: utf-8 -*-

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

version = extract_version_from_pyproject_toml()
app_name = f"RepeatAnalyzer_v{version}.exe"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[('.\\venv\\Lib\\site-packages\\mpl_toolkits\\basemap_data\\*', 'mpl_toolkits\\basemap_data')],
    datas=[('.\\MapData', 'MapData')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
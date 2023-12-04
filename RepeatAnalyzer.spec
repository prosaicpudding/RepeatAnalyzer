# -*- mode: python ; coding: utf-8 -*-

import sys
import os
import platform
from packaging_utils import extract_version_from_pyproject_toml, mpl_toolkits_path

# Get the path to the currently running Python executable
python_executable = sys.executable

version = extract_version_from_pyproject_toml()
app_name = f"RepeatAnalyzer_v{version}"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[(mpl_toolkits_path, os.path.join("mpl_toolkits", "basemap_data"))],
    datas=[('MapData', 'MapData')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    onefile=True,
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

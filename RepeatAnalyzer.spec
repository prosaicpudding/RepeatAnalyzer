# -*- mode: python ; coding: utf-8 -*-

import os

from packaging_utils import extract_version_from_pyproject_toml, mpl_toolkits_path
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules

app_name = f"RepeatAnalyzer"

# Collect dynamic libs and data files from Matplotlib and Basemap
matplotlib_dynlibs = collect_dynamic_libs('matplotlib')
matplotlib_data = collect_data_files('matplotlib', subdir=None)
matplotlib_submodules = collect_submodules('matplotlib')

basemap_dynlibs = collect_dynamic_libs('mpl_toolkits.basemap')
basemap_data = collect_data_files('mpl_toolkits.basemap_data', subdir=None)

pyproj_dynlibs = collect_dynamic_libs('pyproj')
pyproj_data = collect_data_files('pyproj', subdir=None)



a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=matplotlib_dynlibs + basemap_dynlibs + pyproj_dynlibs,
    datas=[('MapData', 'MapData'),('pyproject.toml', 'pyproject.toml')] + matplotlib_data + basemap_data + pyproj_data,
    hiddenimports=matplotlib_submodules,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    # noarchive=False,
    onefile=False,
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

# -*- mode: python ; coding: utf-8 -*-

import os

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

app_name = f"RepeatAnalyzer"

# Collect dynamic libs and data files from Matplotlib and Basemap
#matplotlib_dynlibs = collect_dynamic_libs('matplotlib')
#matplotlib_data = collect_data_files('matplotlib', subdir=None)

#basemap_dynlibs = collect_dynamic_libs('mpl_toolkits.basemap')
basemap_data = collect_data_files('mpl_toolkits.basemap_data', subdir=None)

#pyproj_dynlibs = collect_dynamic_libs('pyproj')
#pyproj_data = collect_data_files('pyproj', subdir=None)
#pillow_dynlibs = collect_dynamic_libs('Pillow')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        ("/usr/local/lib/libtiff.6.dylib", "."), # For Pillow on macos
        ], #matplotlib_dynlibs + basemap_dynlibs + pyproj_dynlibs + copy_metadata('Pillow'),
    datas=[
        ('MapData', 'MapData'), # Map boundaries
        ('pyproject.toml', '.'), # For versioning
        ] + basemap_data, # + pyproj_data + matplotlib_data,
    hiddenimports=[], #matplotlib_submodules,
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

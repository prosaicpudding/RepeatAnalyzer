# -*- mode: python ; coding: utf-8 -*-

import os
import platform

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

app_name = f"RepeatAnalyzer"


basemap_data = collect_data_files('mpl_toolkits.basemap_data', subdir=None)

# Tcl/Tk paths
tcl_path = '/System/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl'
tk_path = '/System/Library/Frameworks/Tk.framework/Tk'

binaries = [] #if platform.system() == 'Windows' else [("/usr/local/lib/libtiff.6.dylib", "pyproj/.dylibs")]# + pyproj_dynlibs
tcl_tk_datas = [] if platform.system() == 'Windows' else [(tcl_path, 'tcl'), (tk_path, 'tk')]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=[
        ('MapData', 'MapData'), # Map boundaries
        ('pyproject.toml', '.'), # For versioning
        ] + basemap_data + tcl_tk_datas,
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

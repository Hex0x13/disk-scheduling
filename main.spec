# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['F:/Assignment/Disk Scheduling/main.py'],
    pathex=[],
    binaries=[],
    datas=[('F:\\Assignment\\Disk Scheduling\\icon.ico', '.'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/CTkMessagebox', 'CTkMessagebox/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/CTkMessagebox-2.5.dist-info', 'CTkMessagebox-2.5.dist-info/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/customtkinter', 'customtkinter/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/customtkinter-5.2.1.dist-info', 'customtkinter-5.2.1.dist-info/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/matplotlib', 'matplotlib/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/matplotlib.libs', 'matplotlib.libs/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/matplotlib-3.8.2.dist-info', 'matplotlib-3.8.2.dist-info/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/numpy', 'numpy/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/numpy.libs', 'numpy.libs/'), ('C:/Users/Asus/AppData/Local/Programs/Python/Python312/Lib/site-packages/numpy-1.26.1.dist-info', 'numpy-1.26.1.dist-info/')],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)

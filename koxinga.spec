# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['koxinga.py'],
    pathex=[],
    binaries=[],
    datas=[('Image', 'Image'), ('Sound', 'Sound'), ('art/cover-reference.png', 'art'), ('wqy-zenhei.ttf', '.')],
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
    name='koxinga',
    icon='koxinga_default.ico',
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
)

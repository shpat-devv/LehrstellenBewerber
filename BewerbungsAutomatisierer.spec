# my_program.spec

# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

# Helper function to recursively gather all files in a directory
def get_datas(directory):
    datas = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            target_path = os.path.join(directory, os.path.relpath(root, start=directory))
            datas.append((file_path, target_path))
    return datas

# List of directories to include
directories = [
    'Bewerbung',
    'changer',
    'help',
    'secretkey',
    'sender',
    'utils'
]

# Generate datas list by gathering all files in each directory
datas = []
for directory in directories:
    datas.extend(get_datas(directory))

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'lxml', 'docx2pdf', 'tqdm', 'lxml.html', 'lxml.cssselect', 'lxml.html.soupparser',
        'lxml.html.html5parser', 'bs4', 'bs4.builder._html5lib', 'html5lib', 'tqdm.notebook',
        'win32com', 'importlib_metadata'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='my_program',
)

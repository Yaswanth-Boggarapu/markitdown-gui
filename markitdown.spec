# markitdown.spec
# PyInstaller spec for MarkItDown GUI — macOS .app bundle

import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[str(Path('app.py').parent.resolve())],
    binaries=[],
    datas=[],
    hiddenimports=[
        'markitdown',
        'markitdown._markitdown',
        'pypdf',
        'pdfminer',
        'pdfminer.high_level',
        'docx',
        'pptx',
        'openpyxl',
        'xlrd',
        'bs4',
        'charset_normalizer',
        'PIL',
        'PIL.Image',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'scipy', 'pandas'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MarkItDown',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MarkItDown',
)

app = BUNDLE(
    coll,
    name='MarkItDown.app',
    icon=None,
    bundle_identifier='com.markitdown.gui',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'Supported Document',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': [
                    'com.adobe.pdf',
                    'org.openxmlformats.wordprocessingml.document',
                    'org.openxmlformats.spreadsheetml.sheet',
                    'org.openxmlformats.presentationml.presentation',
                    'public.html',
                    'public.comma-separated-values-text',
                    'public.json',
                    'public.xml',
                ],
            }
        ],
        'LSMinimumSystemVersion': '11.0',
        'NSHighResolutionCapable': True,
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
    },
)

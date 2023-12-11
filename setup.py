from setuptools import setup

APP = ['renombrar.py']
OPTIONS = {
    'packages': ['os', 'tkinter', 're'],
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'renombrar',
        'CFBundleDisplayName': 'renombrar',
        'CFBundleGetInfoString': "renombrar",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0",
    }
}

setup(
    app=APP,
    name='renombrar',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

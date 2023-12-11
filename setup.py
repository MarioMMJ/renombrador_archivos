from setuptools import setup

APP = ['renombrar.py']
OPTIONS = {
    'packages': ['os', 'tkinter', 're'],
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Renombrador de Archivos',
        'CFBundleDisplayName': 'Renombrador de Archivos',
        'CFBundleGetInfoString': "Renombrador de Archivos",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0",
    }
}

setup(
    app=APP,
    name='Renombrador de Archivos',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

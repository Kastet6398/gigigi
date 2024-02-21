from setuptools import setup

APP = ['guess_the_number_game.py']  # Replace 'your_script.py' with the name of your Python script
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleName': 'Your App Name',
    },
    'packages': ['PyQt5-5.15.9'],  # Add any additional packages or modules your script depends on
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

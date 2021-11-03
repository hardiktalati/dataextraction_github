import setuptools

from src.data_engineering.constants import PROJECT_NAME

setuptools.setup(
    name=PROJECT_NAME,
    version="0.1",
    packages=['src.data_engineering',

              ],
    scripts=['src/data_engineering/main/run_data_processing.py'],
    setup_requires=['wheel'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.json'],
        # And include any *.msg files found in the 'hello' package, too:

    }
)
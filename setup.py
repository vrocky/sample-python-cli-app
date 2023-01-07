from setuptools import setup

setup(
    name='cli_example',
    version='1.0.0',
    packages=['cli_example'],
    entry_points={
        'console_scripts': [
            'myapp = cli_example.main:main',
        ],
    },
)
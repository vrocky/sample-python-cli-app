from setuptools import find_packages, setup

setup(
    name='cli_example',
    version='1.0.0',
    #packages=['cli_example'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest==6.1.2",
    ],
    entry_points={
        'console_scripts': [
            'myapp = cli_example.main:main',
        ],
    },
)
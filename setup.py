from setuptools import setup

setup(
    name='tfl',
    keywords='Transport for London API utility',
    version='0.1',
    url='https://github.com/ali1234/tfl',
    license='GPLv3+',
    packages=['tfl'],
    install_requires=[
        'ansicolors'
    ],
    entry_points={
        'console_scripts': [
            'tfl = tfl.__main__:main'
        ]
    },
)
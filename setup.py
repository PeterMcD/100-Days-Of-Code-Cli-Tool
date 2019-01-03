from setuptools import setup
import re


version = re.search(
    '^__version__ *= *"([.0-9]+)"',
    open('DaysOfCode/bootstrap.py',).read(),
    re.M
).group(1)

setup(
    name='DaysOfCode',
    packages=['DaysOfCode'],
    entry_point={
        'console_scripts': ['DaysOfCode=DaysOfCode.bootstrap:main']
    },
    verion=version,
    url='https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool',
    project_url='https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool',
    author='Peter McDonald',
    author_email='a@b.com',
    maintainer='Peter McDonald',
    maintainer_email='a@b.com',
    classifiers='Programming Language :: Python :: 3',
    licence='MIT',
    description='',
    long_description='',
    keywords=['100 days of code,'
              'programming',
              ],
    platforms=['Linux',
               'Windows',
               ],
)

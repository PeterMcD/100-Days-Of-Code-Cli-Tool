import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('DaysOfCode/bootstrap.py',) as bootstrap:
    version = re.search(
        '^__version__ *= *"([.0-9]+)"',
        bootstrap.read(),
        re.M
    ).group(1)

setuptools.setup(
    name='DaysOfCode',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['doc=DaysOfCode.bootstrap:main',
                            ]
    },
    version=version,
    url='https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool',
    project_url='https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool',
    author='Peter McDonald',
    author_email='a@b.com',
    maintainer='Peter McDonald',
    maintainer_email='a@b.com',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 ],
    licence='MIT',
    description='Package for logging progress in'
                ' the 100 Days Of Code challenge',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['100 days of code,'
              'programming',
              ],
    platforms=['Linux',
               'Windows',
               ],
)

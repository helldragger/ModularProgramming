"""
Installation file
"""

from setuptools import find_packages, setup


# Some vars to reuse the setup file later
PROJECT_NAME = "modular programming"
VERSION = '0.0.5'
URL = 'https://github.com/helldragger/ModularProgramming'
DOWNLOAD_URL = ''
DESCRIPTION = 'Coding for the lazy'
LICENSE = 'AGPL'

LONG_DESCRIPTION = '''Modular programming is a modular style of programming inspired by playing to much with
Factorio's blueprint system'''

setup(name='modular programming',
      version=VERSION,
      author='Christopher Jacquiot',
      author_email='christopher.jacquiot@gmail.com',
      url=URL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6'],
      keywords='development',
      packages=find_packages(exclude=['algorithms', 'docs', 'tests']),
      zip_safe=True)

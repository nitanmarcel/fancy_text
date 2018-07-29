from setuptools import setup
import sys

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only Python 3 is supported at this moment\n If you are using python3 and you get this message try to install the lib with pip3")

setup(
   name='fancy_text',
   version='2.0',
   description='Generate fancy text',
   author='Marcel Alexandru Nitan',
   author_email='nitan.marcel@gmail.com',
   license='MIT',
   packages=['fancy_text'],
   url= 'https://github.com/nitanmarcel/fancy_text',
   keyords = ['fancy', 'fancy_text', 'filter'],
)

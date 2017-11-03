

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
from pkg_resources import parse_requirements


# No need to care about README.md, LICENSE, and requirements.txt files now.

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as f:
    license_str = f.read()

"""

try:
    with open('requirements.txt') as f:
        ireqs = parse_requirements(f.read())
except SyntaxError:
    raise
requirements = [str(req) for req in ireqs]

"""

setup(name='RamPyPackage',
      version='0.1.0',
      description='Developing a python package',
      author='Emory University',
      author_email='rchan31@emory.edu',
      url='https://github.com/cramraj8/RamPyPackage',
      packages=find_packages(),
      package_dir={'rampypackage': 'rampypackage'},
      include_package_data=True,
      # install_requires=requirements,
      # license=license_str,
      zip_safe=False,
      keywords='rampypackage',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Scientific/Engineering :: From Scratch',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )

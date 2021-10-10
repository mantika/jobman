#!/usr/bin/env python
#
#  TODO:
#   * Figure out how to compile and install documentation automatically
#   * Add back in installation requirements
#   * Add download_url

# To enable "python setup.py develop --prefix=~/.local"
# We need to import setuptools
from setuptools import setup

setup(name='Jobman',
      version='2.0.4',
      description=('Facilitate handling of many jobs'
                   '(especially jobs send on cluster)'),
      license='3-clause BSD',
      author='LISA laboratory, University of Montreal, Mantika',
      author_email='theano-user@googlegroups.com',
      url='https://github.com/mantika/jobman',
      packages=['jobman', 'jobman.examples', 'jobman.analyze', 'jobman.dbi'],
      scripts=['bin/jobman', 'bin/jobdispatch'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ])

#!/usr/bin/env python

from distutils.core import setup

setup(name='PyFpdf',
      version='1.54c.1',
      description='Fork of PyFpdf project hosted on Google code',
      author='Mariano Reingart',
      author_email='reingart@gmail.com',
      maintainer='Kevin Turner',
      maintainer_email='kevin@ksturner.com',
      url='http://code.google.com/p/pyfpdf/',
      packages=['pyfpdf'],
      package_data={'pyfpdf': ['invoice.csv']},
      )

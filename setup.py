#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='aws-open',
      version='1.0.0',
      author='Guilherme Victal',
      author_email='guilherme at victal.eti.br',
      url='https://github.com/victal/aws-open',
      description='A set of scripts to open and close SSH on AWS Security groups easily',
      license='MIT',
      packages=['sesame'],
      requires=['requests', 'boto3'],
      entry_points={
            'console_scripts': [
                  'awsesame=sesame.cli:main'
                  ]
            }
        )

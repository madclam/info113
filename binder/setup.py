## -*- encoding: utf-8 -*-
import os
import io
from setuptools import setup
from setuptools.command.install import install

import shutil
class CustomInstallCommand(install):
    def run(self):
        install.run(self)

setup(
    name = "info-114",
    version = "0.1",
    description='Required software for using the Info-114 course material',
    url='http://nicolas.thiery.name/Enseignement/Info114/',
    author='Nicolas M. Thiéry et al.',
    author_email='Nicolas.Thiery@u-psud.fr',
    license='CC',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Information Technology'
      'Topic :: Scientific/Engineering',
      'Programming Language :: C++',
    ], # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    scripts=['bin/info-114'],
    cmdclass={
        'install': CustomInstallCommand,
    },
)

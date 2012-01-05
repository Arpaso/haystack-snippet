### -*- coding: utf-8 -*- ####################################################
"""
Configuration file used by setuptools. It creates 'egg', install all dependencies.
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
        'setuptools',
        'Django',
        'django-haystack>=1.2.6',
        'django-pagination'
]

#Execute function to handle setuptools functionality
setup(name="haystack_snippet",
    version="0.1",
    description="Django application for using haystack search",
    long_description=read('README'),
    author='Arpaso',
    author_email='arvi3d@gmail.com',
    url='http://github.com/Arpaso/haystack-snippet',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=(
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ),
)

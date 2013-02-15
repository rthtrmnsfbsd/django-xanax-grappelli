# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-xanax-grappelli',
    version='0.1.0',
    author='Vishnevski Alexey',
    author_email='vishnevski.a@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://pypi.python.org/pypi/django-xanax-grappelli/',
    license='LICENSE',
    description='Django-xanax-grappelli is a simple integration django-xanax and grappelli.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4.0",
        "django-grappelli >=2.4.3",
        ],
)

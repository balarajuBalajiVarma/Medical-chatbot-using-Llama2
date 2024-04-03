from setuptools import find_packages, setup

setup(
    name="Medical chat bot",
    version="0.0.0",
    author="Balaraju Balaji name",
    author_email="balajivarma.b@gmail.com",
    packages=find_packages(),  # Based on find package it will look for constructor __init__.py file in
                               # entire data folders and  that would consider it as local package

)
import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Python Packages",
    version = "1.0",
    author = "Joel Ranjith Jebansan",
    author_email = "joelranjithjebanesan7@gmail.com",
    description = ("python modules for circle and rectangle to find its area and circumference  "),
    license = "BSD",
    keywords = "Packages distribution",
    url = "http://www.bookconnectsolutions.com/projects/Book",
    packages=['Python Module'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

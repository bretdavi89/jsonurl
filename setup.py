from setuptools import setup, find_packages

#DUMMY COMMENT
setup(
    name = 'jsonurl',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [],
    url = '',
    author = 'Richard Jones',
    author_email = 'richard@cottagelabs.com',
    description = "A library for serialising and deserialising URL query strings which can also be represented as JSON.",
    license = 'CC0',
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)


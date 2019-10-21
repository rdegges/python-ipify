"""
setup.py
~~~~~~~~

Packaging information and tools.
"""


from os.path import abspath, dirname, join, normpath
from subprocess import call
from sys import exit

from setuptools import Command, find_packages, setup


class TestCommand(Command):
    """
    The ``python setup.py test`` command line invocation is powered by this
    helper class.

    This class will run ``py.test`` behind the scenes and handle all command
    line arguments for ``py.test`` as well.
    """
    description = 'run all tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run the test suite."""
        exit(call(['py.test', '--cov-report', 'term-missing', '--cov', 'ipify']))


setup(

    # Basic package information:
    name = 'ipify',
    version = '1.0.1',
    packages = find_packages(exclude=['tests']),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [
        'backoff>=1.0.7',
        'requests>=2.7.0',
    ],
    tests_require = [
        'pytest>=2.7.0',
        'pytest-cov>=1.8.1',
        'python-coveralls>=2.5.0',
    ],

    # Test harness:
    cmdclass = {
        'test': TestCommand,
    },

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/python-ipify',
    keywords = 'python api client ipify ip address public ipv4 ipv6 service',
    description = 'The official client library for ipify: A Simple IP Address API.',
    long_description = open(normpath(join(dirname(abspath(__file__)), 'README.rst'))).read(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

)

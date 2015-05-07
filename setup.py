"""
setup.py
~~~~~~~~

Packaging information and tools.
"""


from subprocess import call
from sys import exit

from setuptools import Command, find_packages, setup

from ipify import __doc__ as description


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
        exit(call(['py.test', '--cov', 'ipify']))


setup(

    # Basic package information:
    name = 'ipify',
    version = '1.0.0',
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
    long_description = description,
    classifiers = [
    ],

)

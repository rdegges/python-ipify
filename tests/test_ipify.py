"""
tests.ipify
~~~~~~~~~~~

All tests for our ipify.ipify module.
"""


from unittest import TestCase

from ipify import __version__
from ipify.ipify import USER_AGENT


class UserAgentTest(TestCase):

    def test_user_agent_contains_library_version(self):
        self.assertTrue(__version__ in USER_AGENT)

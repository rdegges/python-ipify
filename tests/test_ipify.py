"""
tests.ipify.ipify
~~~~~~~~~~~~~~~~~

All tests for our ipify.ipify module.
"""


from unittest import TestCase

from requests.models import Response

from ipify.ipify import _get_ip_resp


class GetIpRespTest(TestCase):
    """Tests for our helper function: ``_get_ip_resp``."""

    def test_returns_response(self):
        self.assertIsInstance(_get_ip_resp(), Response)

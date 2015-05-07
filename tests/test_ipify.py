"""
tests.ipify.ipify
~~~~~~~~~~~~~~~~~

All tests for our ipify.ipify module.
"""


from unittest import TestCase

from requests.models import Response

from ipify.exceptions import ConnectionError, IpifyException, ServiceError
from ipify.ipify import _get_ip_resp, get_ip


class BaseTest(TestCase):
    """A base test class."""

    def setUp(self):
        import ipify
        self._api_uri = ipify.ipify.API_URI

    def tearDown(self):
        import ipify
        ipify.ipify.API_URI = self._api_uri


class GetIpRespTest(BaseTest):
    """Tests for our helper function: ``_get_ip_resp``."""

    def test_returns_response(self):
        self.assertIsInstance(_get_ip_resp(), Response)


class GetIpTest(BaseTest):
    """Tests for our ``get_ip`` function."""

    def test_raises_connection_error_on_connection_error(self):
        import ipify

        ipify.ipify.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsdfsa.com'
        self.assertRaises(ConnectionError, get_ip)

    def test_raises_ipify_exception_on_error(self):
        import ipify

        ipify.ipify.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsdfsa.com'
        self.assertRaises(IpifyException, get_ip)

    def test_raises_service_error_on_error(self):
        # TODO: Make ipify's API service only respond to the root URI -- it
        # should return a 404 for any invalid URIs.
        #import ipify

        #ipify.ipify.API_URI = 'https://api.ipify.org/woo'
        #self.assertRaises(ServiceError, get_ip)
        pass

    def test_raises_service_error_on_empty_body(self):
        # TODO: Find a URI that is valid (returns a 200), but has an empty body.
        pass

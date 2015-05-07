"""
ipify.ipify
~~~~~~~~~~~

The module holds the main ipify library implementation.
"""


from platform import mac_ver, win32_ver, linux_distribution, system
from sys import version_info as vi

from backoff import expo, on_exception
from requests import get
from requests.exceptions import RequestException

from . import __version__
from .exceptions import ConnectionError, ServiceError


# Globals
API_URI = 'https://api.ipify.org'
OS_VERSION_INFO = {
    'Linux': '%s' % (linux_distribution()[0]),
    'Windows': '%s' % (win32_ver()[0]),
    'Darwin': '%s' % (mac_ver()[0]),
}

# The user-agent string is provided so that I can (eventually) keep track of
# what libraries to support over time.  EG: Maybe the service is used primarily
# by Windows developers, and I should invest more time in improving those
# integrations.
USER_AGENT = 'python-ipify/%s python/%s %s/%s' % (
    __version__,
    '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
    system(),
    OS_VERSION_INFO.get(system(), ''),
)

# The maximum amount of tries to attempt when making API calls.
MAX_TRIES = 3


@on_exception(expo, RequestException, max_tries=MAX_TRIES)
def _get_ip_resp():
    """
    Internal function which attempts to retrieve this machine's public IP
    address from the ipify service (http://www.ipify.org).

    :rtype: obj
    :returns: The response object from the HTTP request.
    :raises: RequestException if something bad happened and the request wasn't
        completed.

    .. note::
        If an error occurs when making the HTTP request, it will be retried
        using an exponential backoff algorithm.  This is a safe way to retry
        failed requests without giving up.
    """
    return get(API_URI, headers={'user-agent': USER_AGENT})


def get_ip():
    """
    Query the ipify service (http://www.ipify.org) to retrieve this machine's
    public IP address.

    :rtype: string
    :returns: The public IP address of this machine as a string.
    :raises: ConnectionError if the request couldn't reach the ipify service,
        or ServiceError if there was a problem getting the IP address from
        ipify's service.
    """
    try:
        resp = _get_ip_resp()
    except RequestException:
        raise ConnectionError("The request failed because it wasn't able to reach the ipify service. This is most likely due to a networking error of some sort.")

    if resp.status_code != 200:
        raise ServiceError('Received an invalid status code from ipify:' + resp.status_code + '. The service might be experiencing issues.')
    elif not resp.text:
        raise ServiceError('Received an response from ipify. The service might be experiencing issues.')

    return resp.text

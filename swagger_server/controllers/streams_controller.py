import connexion
import six

from swagger_server.models.stream import Stream  # noqa: E501
from swagger_server import util


def streams_get():  # noqa: E501
    """Get Twitch streams.

    Return stream models. # noqa: E501


    :rtype: List[Stream]
    """
    return 'do some magic!'

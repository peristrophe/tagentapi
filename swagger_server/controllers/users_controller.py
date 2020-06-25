import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def users_user_id_get(user_id):  # noqa: E501
    """Get user by Twitch User ID.

    Return a single user model. # noqa: E501

    :param user_id: Twitch User ID.
    :type user_id: str

    :rtype: List[User]
    """
    return 'do some magic!'

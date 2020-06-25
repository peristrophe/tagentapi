# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.stream import Stream  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStreamsController(BaseTestCase):
    """StreamsController integration test stubs"""

    def test_streams_get(self):
        """Test case for streams_get

        Get Twitch streams.
        """
        response = self.client.open(
            '/v1/streams',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

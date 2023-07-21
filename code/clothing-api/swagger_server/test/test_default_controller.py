# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.clothing_article import ClothingArticle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_clothing_get(self):
        """Test case for clothing_get

        Retrieve a list of clothing articles
        """
        response = self.client.open(
            '/clothing',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clothing_post(self):
        """Test case for clothing_post

        Add a new clothing article
        """
        article = ClothingArticle()
        response = self.client.open(
            '/clothing',
            method='POST',
            data=json.dumps(article),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

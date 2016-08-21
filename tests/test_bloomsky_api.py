#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bloomsky_api
----------------------------------

Tests for `bloomsky_api` module.
"""

import json
import responses
import unittest

import bloomsky_api
from .testing_data import GOOD_API_RESPONSE, GOOD_DATA_RESPONSE_JSON

class TestBloomskyAPI(unittest.TestCase):

    @responses.activate
    def test_package(self):
        url = bloomsky_api.bloomsky_api.DEFAULT_API_URL
        responses.add(responses.GET, url,
                  body=GOOD_API_RESPONSE, status=200,
                  content_type='application/json')
        client = bloomsky_api.BloomSkyAPIClient(api_key='totally-fake-key')
        data = client.get_data()
        assert(data == json.loads(str(GOOD_DATA_RESPONSE_JSON)))

    def tearDown(self):
        pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bloomsky_api
----------------------------------

Tests for `bloomsky_api` module.
"""

import json
import responses

import bloomsky_api
from .testing_data import GOOD_API_RESPONSE, GOOD_DATA_RESPONSE_JSON

class TestBloomskyAPI(object):

    def setup(self):
        self.url = bloomsky_api.bloomsky_api.DEFAULT_API_URL
        self.client = bloomsky_api.BloomSkyAPIClient(api_key='totally-fake-key')

    @responses.activate
    def test_getting_data(self):
        responses.add(responses.GET, self.url,
                  body=GOOD_API_RESPONSE, status=200,
                  content_type='application/json')
        data = self.client.get_data()
        assert(data == json.loads(str(GOOD_DATA_RESPONSE_JSON)))


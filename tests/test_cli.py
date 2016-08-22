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
from click.testing import CliRunner

import bloomsky_api.cli
from .testing_data import GOOD_API_RESPONSE, GOOD_CLI_OUTPUT_JSON

class TestBloomskyCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    @responses.activate
    def test_cli(self):
        url = bloomsky_api.bloomsky_api.DEFAULT_API_URL
        responses.add(responses.GET, url,
                  body=GOOD_API_RESPONSE, status=200,
                  content_type='application/json')
        result = self.runner.invoke(
                bloomsky_api.cli.cli, ['--api-key', 'key-would-go-here'])
        output = json.loads(result.output)
        assert(output == json.loads(str(GOOD_CLI_OUTPUT_JSON)))


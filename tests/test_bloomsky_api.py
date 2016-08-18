#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bloomsky_api
----------------------------------

Tests for `bloomsky_api` module.
"""

import unittest

import bloomsky_api


class TestBloomsky_api(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(bloomsky_api.__version__)

    def tearDown(self):
        pass

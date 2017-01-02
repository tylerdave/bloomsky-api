#!/usr/bin/env python
import os
import pytest
from click.testing import CliRunner

from bloomsky_api import cli

def is_travis_but_not_cron_or_api():
    return os.environ.get('TRAVIS_EVENT_TYPE') not in ['api', 'cron', None]

@pytest.mark.skipif(is_travis_but_not_cron_or_api(),
        reason='Running via Travis but not a cron')
class TestClickTutorial(object):

    def setup(self):
        self.runner = CliRunner()

    # FIXME: check more of the output and define valid values via env vars
    def test_outputs_api_response(self):
        result = self.runner.invoke(cli.cli, [])
        print(result.output)
        assert '"street_name": "Lakeland Avenue"' in result.output


import os
import requests

DEFAULT_API_URL = 'https://thirdpartyapi.appspot.com/api/skydata/'

class BloomSkyClient(object):
    """ A client for interacting with the BloomSky API """

    def __init__(self, api_key=None, api_url=None):
        self.api_key = self._get_api_key(api_key)
        self.api_url = self._get_api_url(api_url)

    def get_data(self):
        headers = {'Authorization': self.api_key}
        response = requests.get(self.api_url, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _get_api_key(provided_api_key=None):
        if provided_api_key is not None:
            return provided_api_key
        return os.environ.get('BLOOMSKY_API_KEY')
        # TODO: consider looking for key in config file too?

    @staticmethod
    def _get_api_url(provided_api_url=None):
        if provided_api_url is not None:
            return provided_api_url
        else:
            return DEFAULT_API_URL


===============================
BloomSky API
===============================

.. image:: https://img.shields.io/travis/tylerdave/bloomsky-api.svg
        :target: https://travis-ci.org/tylerdave/bloomsky-api

.. image:: https://img.shields.io/pypi/v/bloomsky-api.svg
        :target: https://pypi.python.org/pypi/bloomsky-api

.. image:: https://coveralls.io/repos/github/tylerdave/bloomsky-api/badge.svg?branch=master
    :target: https://coveralls.io/github/tylerdave/bloomsky-api?branch=master

.. image:: https://readthedocs.org/projects/bloomsky-api/badge/?version=latest
    :target: http://bloomsky-api.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

A simple Python client for the BloomSky API.

*Note: Neither this package nor its maintainer are affiliated with BloomSky.*

For more information about the BloomSky device and its API, see: 
http://weatherlution.com/bloomsky-api/


Prerequisites
-------------

* Python (2.7, 3.3, 3.4, 3.5)
* BloomSky API key (get it here: https://dashboard.bloomsky.com/)

Getting Started
---------------

Installation
~~~~~~~~~~~~

.. code-block:: bash

  pip install BloomSky-API

To install optional command-line interface (requires click):

.. code-block:: bash

  pip install BloomSky-API[cli]


Usage
~~~~~

You can either store the API key in an environment variable named
`BLOOMSKY_API_KEY` or provide it as an argument when creating the client.

**Stored in environment variable:**

.. code-block:: python

  import bloomsky_api
  client = bloomsky_api.BloomSkyAPIClient()
  data = client.get_data()

**Provided via argument:**
  
.. code-block:: python

  import bloomsky_api
  client = bloomsky_api.BloomSkyAPIClient(api_key='Your-real-API-key-goes-here')
  data = client.get_data()


Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

If you install the optional command-line interface, the `bloomsky-api` command will be available. Usage:

.. code-block:: none

  Usage: bloomsky-api [OPTIONS]
  
    Retrieve data from the BloomSky API and output it as JSON.
  
  Options:
    --api-key TEXT         BloomSky API key (can be set via env var
                           BLOOMSKY_API_KEY).
    --api-url TEXT         Override BloomSky API endpoint URL.
    --json-indent INTEGER  Number of spaces to indent nested JSON levels.
    -i, --intl-units       Use SI units instead of the default US.
    --raw                  Return raw response instead of remapped keys.
    --help                 Show this message and exit.


Data
~~~~

The returned data contains all of the information from the API response but
with more Pythonic names and data types.


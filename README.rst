===============================
BloomSky API
===============================

.. image:: https://img.shields.io/travis/tylerdave/bloomsky-api.svg
        :target: https://travis-ci.org/tylerdave/bloomsky-api

.. image:: https://img.shields.io/pypi/v/bloomsky-api.svg
        :target: https://pypi.python.org/pypi/bloomsky-api


A simple Python client for the BloomSky API.

*Note: This package and its maintainer are not affiliated with BloomSky and/or
Weatherlution*

For more information about the BloomSky device and its API, see: 
http://weatherlution.com/bloomsky-api/



Prerequisites
-------------

* Python (2.7, 3.3, 3.4, 3.5)
* BloomSky API key (get it here)

Installation
------------

```
pip install BloomSky-API
```

Usage
-----


```
from bloomsky_api import bloomsky_api
client = bloomsky_api.BloomSkyClient()
data = client.get_data()
```




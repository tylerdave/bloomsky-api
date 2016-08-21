========
Usage
========

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


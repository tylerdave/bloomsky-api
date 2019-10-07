class BloomSkyAPIError(Exception):
    pass

class APIKeyMissing(BloomSkyAPIError):
    pass

class APIKeyInvalid(BloomSkyAPIError):
    pass

class BloomSkyConnection(BloomSkyAPIError):
    pass

class NoDevicesFound(BloomSkyAPIError):
    pass

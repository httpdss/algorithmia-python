"""
Algorithmia API Client (python)
"""

import os

from Algorithmia.client import Client

apiKey = None
apiAddress = None


def algo(algoRef):
    """
    Get reference to an algorithm using a default client
    """

    # Return algorithm reference using default client
    return getDefaultClient().algo(algoRef)


def file(dataUrl):
    return getDefaultClient().file(dataUrl)


def dir(dataUrl):
    return getDefaultClient().dir(dataUrl)


def client(api_key=None, api_address=None):
    return Client(api_key, api_address)

# The default client to use, assuming the
# user does not want to construct their own
defaultClient = None


def getDefaultClient():
    """
    Used internally to get default client
    """

    global defaultClient
    
    # Check for default client, and ensure default API key has not changed
    if defaultClient is None or defaultClient.apiKey is not apiKey:
        # Construct default client
        defaultClient = Client(apiKey)
    return defaultClient


def getApiAddress():
    """
    Used internally to get default api client
    """

    global apiAddress
    if apiAddress is not None:
        # First check for user setting Algorithmia.apiAddress = "XXX"
        return apiAddress
    elif 'ALGORITHMIA_API' in os.environ:
        # Then check for system environment variable
        return os.environ['ALGORITHMIA_API']
    else:
        # Else return default
        return "https://api.algorithmia.com"

class AsyncResponse(object):
    """
    Response from the API for an asynchronous request (output=void)
    """

    def __init__(self, server_response):
        self.async_protocol = server_response['async']
        self.request_id = server_response['request_id']

    def __repr__(self):
        return 'AsyncResponse(async_protocol={0}, request_id={1})'.format(self.async_protocol,
                                                                          self.request_id)

class HubError(OSError):
    pass


class AuthorizationError(HubError):
    pass


class ConnectionError(HubError):
    """Hub connection error"""

    pass
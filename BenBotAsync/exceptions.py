class BenBotException(Exception):
    pass


class InvalidParameters(BenBotException):
    pass


class NotFound(BenBotException):
    pass


class InvalidVersion(BenBotException):
    pass

__author__ = 'maximmillen'


class SignalProcessingError(Exception):
    pass


class SignalProcessingWarning(Warning):
    pass


def deprecation(message):
    warnings.warn(message, stacklevel=3)
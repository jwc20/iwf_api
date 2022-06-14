from .core import *
from .event import Event
from .result import Result
from .athlete import Athlete


class Iwf(Event, Result, Athlete):
    def __init__(self, keywords=[], *args):
        Event.__init__(self, keywords=keywords, *args)
        Result.__init__(self, keywords=keywords, *args)
        Athlete.__init__(self, keywords=keywords, *args)


__version__ = "0.0.1"
__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/iwf-api/"
__license__ = "MIT"

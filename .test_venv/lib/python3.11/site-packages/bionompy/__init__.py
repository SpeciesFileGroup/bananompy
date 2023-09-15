from .package_metadata import __author__, __license__, __version__, __title__
from .bionompy import agent, occurrence, parse, person, suggest
from .utils import bionompy_utils

import logging
from logging import NullHandler
logging.getLogger(__name__).addHandler(NullHandler())
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
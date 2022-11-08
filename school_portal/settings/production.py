# NOTE default wagtail import
from .base import *  # noqa: F403, F401

DEBUG = False

try:
    # NOTE default wagtail import
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

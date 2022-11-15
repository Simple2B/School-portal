# NOTE default wagtail import
from .base import *  # noqa: F403, F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!
# TODO define correct hosts
# ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    # NOTE default wagtail import
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

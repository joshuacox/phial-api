from .base import *

DEBUG = True

UPLOAD_DIRECTORY="mauifloralcom/static/media"

try:
	from .local import *
except ImportError:
	pass

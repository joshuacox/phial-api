from .base import *

DEBUG = True
INTERNAL_IPS = ('50.134.190.135')
try:
	from .local import *
except ImportError:
	pass

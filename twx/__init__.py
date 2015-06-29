import sys

"""
Expand the tex namespace
"""
if sys.version_info[0] == 3 and sys.version_info[1] >=2:
	from pkgutil import extend_path
	__path__ = extend_path(__path__, __name__)

"""
Only import twx modules on supported pytohn versions. Type hinting breaks testing 2.7 against twx.botapi
"""
if sys.version_info[0] == 3 and sys.version_info[1] >=4:
	from . twx import *


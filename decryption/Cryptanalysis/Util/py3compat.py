__revision__ = "$Id$"

import sys

if sys.version_info[0] == 2:
    def b(s):
        return s
    def bchr(s):
        return chr(s)
    def bstr(s):
        return str(s)
    def bord(s):
        return ord(s)
    if sys.version_info[1] == 1:
        def tobytes(s):
            try:
                return s.encode('latin-1')
            except:
                return ''.join(s)
    else:
        def tobytes(s):
            if isinstance(s, str):
                return s.encode("latin-1")
            else:
                return ''.join(s)
else:
    def b(s):
       return s.encode("latin-1") # utf-8 would cause some side-effects we don't want
    def bchr(s):
        return bytes([s])
    def bstr(s):
        if isinstance(s,str):
            return bytes(s,"latin-1")
        else:
            return bytes(s)
    def bord(s):
        return s
    def tobytes(s):
        if isinstance(s,bytes):
            return s
        else:
            if isinstance(s,str):
                return s.encode("latin-1")
            else:
                return bytes(s)
"""Module with definitions common to all block ciphers."""

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Cryptanalysis.Util.py21compat import *
from Cryptanalysis.Util.py3compat import *

#: CounTer Mode (CTR). See `blockalgo.MODE_CTR`.
MODE_CTR = 6

def _getParameter(name, index, args, kwargs, default=None):
    """Find a parameter in tuple and dictionary arguments a function receives"""
    param = kwargs.get(name)
    if len(args)>index:
        if param:
            raise ValueError("Parameter '%s' is specified twice" % name)
        param = args[index]
    return param or default
    
class BlockAlgo:
    """Class modelling an abstract block cipher."""

    def __init__(self, factory, key, *args, **kwargs):
        self.mode = _getParameter('mode', 0, args, kwargs, default=MODE_CTR)
        self.block_size = factory.block_size
        self._cipher = factory.new(key, *args, **kwargs)

    def encrypt(self, plaintext):
        return self._cipher.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self._cipher.decrypt(ciphertext)
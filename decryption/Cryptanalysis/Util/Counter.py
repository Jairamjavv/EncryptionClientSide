import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Cryptanalysis.Util.py21compat import *
from Cryptanalysis.Util.py3compat import *
from Cryptanalysis.Util import _counter
import struct

# Factory function
def new(nbits, prefix=b(""), suffix=b(""), initial_value=1, overflow=0, little_endian=False, allow_wraparound=False, disable_shortcut=False):
    # Sanity-check the message size
    (nbytes, remainder) = divmod(nbits, 8)
    if remainder != 0:
        # In the future, we might support arbitrary bit lengths, but for now we don't.
        raise ValueError("nbits must be a multiple of 8; got %d" % (nbits,))
    if nbytes < 1:
        raise ValueError("numbernbits too small")
    elif nbytes > 0xffff:
        raise ValueError("nbits too large")

    initval = _encode(initial_value, nbytes, little_endian)

    if little_endian:
        return _counter._newLE(bstr(prefix), bstr(suffix), initval, allow_wraparound=allow_wraparound, disable_shortcut=disable_shortcut)
    else:
        return _counter._newBE(bstr(prefix), bstr(suffix), initval, allow_wraparound=allow_wraparound, disable_shortcut=disable_shortcut)

def _encode(n, nbytes, little_endian=False):
    retval = []
    n = int(n)
    for i in range(nbytes):
        if little_endian:
            retval.append(bchr(n & 0xff))
        else:
            retval.insert(0, bchr(n & 0xff))
        n >>= 8
    return b("").join(retval)
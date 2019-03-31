from Cryptanalysis.Cipher import blockalgo
from Cryptanalysis.Cipher import _AES

class AESCipher (blockalgo.BlockAlgo):
    """AES cipher object"""

    def __init__(self, key, *args, **kwargs):
        """Initialize an AES cipher object
        
        See also `new()` at the module level."""
        blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)

def new(key, *args, **kwargs):
    """Create a new AES cipher"""
    return AESCipher(key, *args, **kwargs)

#: CounTer Mode (CTR). See `blockalgo.MODE_CTR`.
MODE_CTR = 6
#: Size of a data block (in bytes)
block_size = 16

#: Size of a key (in bytes)
key_size = ( 16, 24, 32 )
import base64
import hashlib
import string, sys

from Fingerprint import Fingerprint


keyfile = sys.argv[1]
(key_type, keyencoded, _) = file(keyfile, 'r').read().split(' ', 2)
key = base64.decodestring(keyencoded)
hexstring = hashlib.sha256(key).hexdigest()
hash_values = [int(hexstring[i:i+8], 16) for i in range(0,len(hexstring), 8)]
print Fingerprint(hash_values)

import base64
import hashlib
import string
import math
import argparse, sys

from Fingerprint import Fingerprint


def get_key_typestring(key_type):
    return {
        'ssh-rsa': 'RSA',
        'ssh-dss': 'DSA',
        'ecdsa-sha2-nistp256': 'ECDSA 256',
    }.get(key_type)

def get_rsa_key_length(keyraw):
    keyHex = keyraw.encode('hex')
    start = 8
    typeLength = int(keyHex[0:start], 16)
    start += typeLength*2
    lengthExponent = int(keyHex[start:start+8], 16)
    start += 8+2*lengthExponent;
    lengthKey = int(keyHex[start:start+8], 16)
    start +=8
    key =keyHex[start: start + 2* lengthKey]
    n = int(key, 16)
    return int(math.log(n, 2)) + 1


def main(argv):
    parser = argparse.ArgumentParser(description='Draw a random art image for a ssh key.')
    parser.add_argument('filehandle', metavar='N', type=file,
                    help='an integer for the accumulator')
    parser.add_argument('-M', dest='hash', action='store_const',
                       const='MD5', default='SHA256',
                       help='hash function to use (default: SHA256')
    args = parser.parse_args()
    (key_type, keyencoded, _) = args.filehandle.read().split(' ', 2)
    key = base64.decodestring(keyencoded)

    hexstring = {
        'SHA256': hashlib.sha256(key).hexdigest(),
        'MD5': hashlib.md5(key).hexdigest()
    }[args.hash]

    print base64.encodestring(hashlib.sha256(key).digest())
    hash_values = [int(hexstring[i:i+8], 16) for i in range(0,len(hexstring), 8)]
    key_description = get_key_typestring(key_type)
    if 'ssh-rsa' == key_type:
        key_description += " %s" % get_rsa_key_length(key)
    print Fingerprint(hash_values, key_description, args.hash)


if __name__ == "__main__":
    main(sys.argv[1:])

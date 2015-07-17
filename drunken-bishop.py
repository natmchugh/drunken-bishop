import base64
import hashlib
import string
import argparse, sys

from Fingerprint import Fingerprint


def get_key_typestring(key_type):
    return {
        'ssh-rsa': 'RSA',
        'ssh-dss': 'DSA',
        'ecdsa-sha2-nistp256': 'ECDSA 256',
    }.get(key_type)

def get_key_length(keyraw):
    keyHex = keyraw.encode('hex')
    typeLength = int(keyHex[0:8], 16)
    type = keyraw[4:typeLength+4]

    lengthExponent = int(keyHex[8+typeLength*2:16+typeLength*2], 16)

    lengthKey = int(keyHex[8+typeLength*2+lengthExponent*2:16+lengthExponent*2+typeLength*2], 16)


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
    get_key_length(key)

    hexstring = {
        'SHA256': hashlib.sha256(key).hexdigest(),
        'MD5': hashlib.md5(key).hexdigest()
    }[args.hash]
    hash_values = [int(hexstring[i:i+8], 16) for i in range(0,len(hexstring), 8)]
    print Fingerprint(hash_values, get_key_typestring(key_type), args.hash)


if __name__ == "__main__":
    main(sys.argv[1:])

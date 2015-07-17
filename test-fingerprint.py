import unittest

from Fingerprint import Fingerprint

class TestFigerprint(unittest.TestCase):

    def test_get_movements(self):
        fingerprint = Fingerprint([0xb53f208a, 0x2f95a90a, 0xfb9bd053, 0x6ff99733], 'RSA 2048', 'MD5')
        me = open('natmchugh.txt', 'r').read()
        print str(fingerprint)
        self.assertEqual(str(fingerprint), me)

    def test_hash_to_moves(self):
        fingerprint = Fingerprint([0xfc94b0c1], 'RSA 2048', 'MD5')
        expected = [0,3,3,3,  0,1,1,2, 0,0,3,2, 1,0,0,3]
        actual = fingerprint.hash_to_moves([0xfc94b0c1])
        self.assertEqual(actual, expected)
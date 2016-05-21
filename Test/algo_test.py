import sys
import unittest
import os

sys.path.append("../")

import Algorithmia


class AlgoTest(unittest.TestCase):

    def setUp(self):
        self.client = Algorithmia.client(os.environ['ALGORITHMIA_API_KEY'])

    def test_call_binary(self):
        result = self.client.algo('pmcq/Python2xEcho/0.1.0').pipe(bytearray('foo','utf-8'))
        self.assertEquals('binary', result.metadata.content_type)
        self.assertEquals(bytearray('foo','utf-8'), result.result)

if __name__ == '__main__':
    unittest.main()

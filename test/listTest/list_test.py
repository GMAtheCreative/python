import unittest

from listPlayGround.list import dictionary


class TestList(unittest.TestCase):
    def test_that_list_in_multiple(self):
        self.assertEqual(dictionary([1,2,3,4,5]), {1:1,2:8,3:27,4:64,5:125})

"""
Unittests for the cat module
"""
import sys
import types
import unittest

#from mock import MagicMock, patch

if sys.version_info <  (2, 7): import unittest2 as unittest

import cat

class BoxTestCase(unittest.TestCase):
    def setUp(self):
        class Frist(object):
            def sayhai(self):
                return 'hai'

        class Other(object):
            def saybai(self):
                return 'bai'

        class HeisenThing(cat.Box):
            box = [Frist, Other]

        self.klass = HeisenThing
        self.inst = HeisenThing()
        self.Frist = Frist
        self.Other = Other

    def test_isinstance(self):
        "Should be both"
        self.assertIsInstance(self.inst, self.Frist)
        self.assertIsInstance(self.inst, self.Other)

    # def test_method(self):
    #     "Should have both"
    #     self.assertIsInstance(self.inst.sayhai, types.MethodType)
    #     self.assertIsInstance(self.inst.saybai, types.MethodType)

    # def test_execute_method(self):
    #     "Should return"
    #     self.assertEqual('hai', self.inst.sayhai())

    # def test_resolves(self):
    #     "Should resolve"
    #     self.inst.sayhai()
    #     self.assertIsNotInstance(self.inst, self.Other)
    #     self.assertIsInstance(self.inst, self.Frist)
    #     with self.assertRaises(AttributeError):
    #         m = self.inst.saybai


if __name__ == '__main__':
    unittest.main()


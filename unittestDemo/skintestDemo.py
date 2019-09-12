#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("skip whatever")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2, "if True skip test")
    def test_skip_if(self):
        print("test bbb")

    @unittest.skipUnless(3 > 2, "if True excute test")
    def test_skip_unless(self):
        print("test ccc")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2, 3)

if __name__ == '__main__':
    unittest.main()
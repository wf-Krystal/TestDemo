#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest

class Test001_Fail(unittest.TestCase):
    #测试用例前执行
    def setUp(self):
        print('Case Befor')
        pass

    #测试用例后执行
    def tearDown(self):
        print('Case After')
        pass
    #testcase1
    def test_Case1(self):
        a = 3
        b = 2
        self.assertEqual(a + b, 4, 'Result Failed')

    #testcase2
    def test_Case2(self):
        a = 3
        b = 2
        self.assertEqual(a * b, 7, 'Result Failed')

if __name__ == '__main__':
    unittest.mian()
